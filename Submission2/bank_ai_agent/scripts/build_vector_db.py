from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

with open("data/banking_faqs.txt", "r", encoding="utf-8") as f:
    content = f.read()

faq_entries = [
    faq.strip()
    for faq in content.split("\n\n")
    if faq.strip()
]

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_texts(
    texts=faq_entries,
    embedding=embedding,
    persist_directory="vector_store/chroma_db"
)

db.persist()

print(f"Created {len(faq_entries)} FAQ vectors.")