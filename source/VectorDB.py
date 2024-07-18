from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from DataLoader import DataLoader
import chromadb

# Creating Vector Database
class VectorDB:
    """
    Custome Vector Database using ChromaDB.
    """
    def __init__(self):
        self.client = chromadb.PersistentClient(path='./chroma')
        self.document = DataLoader().UnStructuredPDFLoader()

    # Creating Chroma Collection (If not exists)
    def create_collection(self):
        col_doc = []
        col_meta_data = []
        
        # Creating Empty Collection
        self.collection = self.client.create_collection(name='WHR_db')
        for ind, doc in enumerate(self.document):
          col_doc.append(doc.page_content)
          doc.metadata['languages']=doc.metadata['languages'][0]
          col_meta_data.append(doc.metadata)
            
        # Adding documents along with metadata
        self.collection.add(
                documents=col_doc,
                metadatas=col_meta_data,
                ids=[f'ids{i}' for i in range(len(self.document))])

    # Loading WHR_db collection (if exists)
    def load_collection(self):
        # Checking existence of collection
        existing_collections = [col.name for col in self.client.list_collections()]
        if 'WHR_db' not in existing_collections:
            self.create_collection()
        else:
            pass
            
        # Creating Retriever
        db = Chroma(
            collection_name='WHR_db',
            embedding_function=SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2'),
            client=self.client
        )
        retriever = db.as_retriever()

        return retriever
        