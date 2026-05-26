from app.services.retrieval import retrieve_chunks
from app.services.llm import ask_llm

from app.services.memory import (
    save_message,
    get_memory
)

def rag_pipeline(question, session_id):

    chunks = retrieve_chunks(question)

    context = "\n".join(chunks)

    memory = get_memory(session_id)

    history = ""

    for msg in memory:

        history += f"{msg['role']}: {msg['message']}\n"

    prompt = f"""
    You are a helpful AI assistant.

    Previous Conversation:
    {history}

    Context:
    {context}

    User Question:
    {question}
    """

    answer = ask_llm(prompt)

    save_message(
        session_id,
        "user",
        question
    )

    save_message(
        session_id,
        "assistant",
        answer
    )

    return {
        "reply": answer,
        "retrievedChunks": len(chunks)
    }