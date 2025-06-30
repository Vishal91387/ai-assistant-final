from langchain_community.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQAWithSourcesChain
from config import CHROMA_PATH, chroma_settings

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectordb = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings,
    collection_name="my_rag_docs",
    client_settings=chroma_settings
)

retriever = vectordb.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.3, "k": 5})

llm = Ollama(model="llama3:8b", num_predict=512)

qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

def ask_question_from_docs(query):
    result = qa_chain({"question": query})
    answer = result.get("answer", "⚠️ No answer found.")
    sources = result.get("source_documents", [])
    source_list = set(doc.metadata.get("source", "") for doc in sources)
    sources_text = "\n".join(f"- {s}" for s in sorted(source_list)) if source_list else "No sources found."
    return f"📘 **Answer**\n{answer}\n\n📚 **Sources:**\n{sources_text}"
