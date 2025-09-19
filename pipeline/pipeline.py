# from src.vector_store import VectorStoreBuilder
# from src.recommender import AnimeRecommender
# from config.config import GROQ_API_KEY, MODEL_NAME
# from utils.logger import get_logger
# from utils.custom_exception import CustomException

# logger = get_logger(__name__)

# class AnimeRecommendationPipeline:
#     def __init__(self, persist_dir: str = "chroma_db"):
#         try:
#             logger.info("Initializing Recommendation Pipeline..")

#             vector_builder = VectorStoreBuilder(csv_path="data/anime_updated.csv", persist_directory=persist_dir)

#             retriever = vector_builder.load_vectorstore().as_retriever()

#             self.recommender = AnimeRecommender(
#                 retriever=retriever,
#                 api_key=GROQ_API_KEY,
#                 model_name=MODEL_NAME
#             )
#             logger.info("Pipeline initialized successfully..")
#         except Exception as e:
#             logger.error(f"Error initializing AnimeRecommendationPipeline: {e}")
#             raise CustomException(e)

#     def recommend(self, query: str) -> str:
#         """Get anime recommendations based on the user's query."""
#         try:
#             logger.info(f"Generating recommendations for query: {query}")
#             recommendations = self.recommender.get_recommendation(query)
#             logger.info("Recommendations generated successfully..")
#             return recommendations
#         except Exception as e:
#             logger.error(f"Error generating recommendations: {e}")
#             raise CustomException(e)

from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Intializing Recommdation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="" , persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization" , e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)
        


        