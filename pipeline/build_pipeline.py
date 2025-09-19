from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the build pipeline...")

        # Load and preprocess data
        data_loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = data_loader.load_and_process()
        logger.info(f"Loaded and processed the dataset.")

        # Build and persist vector store
        logger.info("About to build and save vector store...")
        vector_builder = VectorStoreBuilder(processed_csv)
        logger.info("VectorStoreBuilder initialized.")
        vector_builder.build_and_save_vectorstore()
        logger.info("build_and_save_vectorstore() call completed.")

        logger.info("Vector store built and persisted successfully...")

        logger.info("Build pipeline completed successfully.")
    except Exception as e:
        logger.error(f"Error in build pipeline: {e}")
        raise CustomException(e)
    

if __name__ == "__main__":
    main()