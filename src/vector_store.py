# from langchain.text_splitter import CharacterTextSplitter
# # from langchain.vectorstores import Chroma
# # from langchain_community.vectorstores import Chroma
# from langchain_chroma import Chroma
# from langchain_community.document_loaders.csv_loader import CSVLoader
# from langchain_huggingface import HuggingFaceEmbeddings

# from dotenv import load_dotenv
# load_dotenv()

# class VectorStoreBuilder:
#     def __init__(self, csv_path: str, persist_directory: str="chroma_db"):
#         self.csv_path = csv_path
#         self.persist_directory = persist_directory
#         self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#     def build_and_save_vectorstore(self):
#         from utils.logger import get_logger
#         logger = get_logger(__name__)
#         logger.info("Starting build_and_save_vectorstore()...")
#         loader = CSVLoader(file_path=self.csv_path, encoding='utf-8', metadata_columns=[])
#         logger.info("CSVLoader initialized. Loading data...")
#         data = loader.load()
#         logger.info(f"Loaded {len(data)} documents from CSV.")

#         text_splitter = CharacterTextSplitter(
#             # separator="\n",
#             chunk_size=1000,
#             chunk_overlap=0
#             # ,length_function=len
#         )
#         logger.info("TextSplitter initialized. Splitting documents...")
#         texts = text_splitter.split_documents(data)
#         logger.info(f"Split into {len(texts)} text chunks.")

#         # embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#         logger.info("Creating Chroma vector store from documents...")
#         # Step 1: Create an empty Chroma vector store
#         vector_store = Chroma(persist_directory=self.persist_directory, embedding_function=self.embeddings)
#         logger.info("Empty Chroma vector store created.")
#         # Step 2: Add documents to the vector store
#         vector_store.add_documents(texts)
#         logger.info(f"Added {len(texts)} documents to Chroma vector store.")
#         # Step 3: Persist the vector store
#         logger.info("Persisting vector store to disk...")
#         vector_store.persist()
#         logger.info("Vector store created and persisted successfully.")
    
#     def load_vectorstore(self):
#         """Load an existing vector store from the persist directory."""
#         return Chroma(
#             persist_directory=self.persist_directory,
#             embedding_function=self.embeddings
#         )


from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()


class VectorStoreBuilder:
    def __init__(self,csv_path:str=None,persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    
    def build_and_save_vectorstore(self):
        from utils.logger import get_logger
        logger = get_logger(__name__)
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )

        data = loader.load()
        logger.info(f"Loaded {len(data)} documents from CSV.")

        splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        texts = splitter.split_documents(data)
        logger.info(f"Split into {len(texts)} text chunks.")

        db = Chroma.from_documents(texts,self.embedding,persist_directory=self.persist_dir)
        db.persist()

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir,embedding_function=self.embedding)




