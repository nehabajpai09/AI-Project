import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class RAGTool:

    def __init__(self):

        self.persist_directory = "vector_store/chroma_db"

        if not os.path.exists(self.persist_directory):
            raise FileNotFoundError(
                "Chroma database not found. "
                "Run build_vector_db.py first."
            )

        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=embedding
        )

    def run(self, query):

        results = self.db.similarity_search_with_score(
            query,
            k=1
        )

        if not results:
            return (
                "I could not find reliable banking information."
            )

        doc, score = results[0]

        #print(f"Debug Score: {score}")

        return doc.page_content