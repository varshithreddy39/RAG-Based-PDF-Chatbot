from core.extract_text import extract_text_from_pdf
from core.clean_text import clean_text
from core.chunk_text import chunk_text
from core.build_context import build_context
from core.embeddings import embed_chunks, embed_query                        
from core.vectordb import build_vector_db, search_vector_db
from core.llm import call_llm
from core.prompt import build_prompt
from dotenv import load_dotenv


load_dotenv()
def answer_question(pdf, query):
    greetings =['Hello!','Hi there!','Good day!','Welcome!','Good morning!','Good afternoon!','Good evening!',]
    if query in greetings:
        return "Hello! How can I assist you with the document today?"
    text=extract_text_from_pdf(pdf)
    cleaned_text=clean_text(text)
    text_chunks=chunk_text(cleaned_text)
    embeddings = embed_chunks(text_chunks)
    index=build_vector_db(embeddings)
    query_embedding=embed_query(query)
    top_k_ids, scores=search_vector_db(index, query_embedding, top_k=3)
    relevant_chunks=[text_chunks[i] for i in top_k_ids]
    context=build_context(relevant_chunks)
    prompt=build_prompt(context, query)
    answer=call_llm(prompt)
    return answer


    