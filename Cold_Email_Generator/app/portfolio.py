import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        try:
            # Initialize chroma client for persistent storage
            self.chroma_client = chromadb.PersistentClient('vectorstore')
        except Exception as e:
            print(f"Error initializing ChromaDB client: {e}")
            raise

        # Get or create a collection within ChromaDB
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        # Check if the collection is empty before loading data
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        try:
            # Query the ChromaDB collection for the top 2 most similar documents
            # Extract links from the metadata
           return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
        except Exception as e:
            print(f"Error querying ChromaDB: {e}")
            return []
