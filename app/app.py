# import streamlit as st
# from pipeline.pipeline import AnimeRecommendationPipeline
# from dotenv import load_dotenv

# load_dotenv()

# st.set_page_config(page_title="Anime Recommender", page_icon=":robot_face:", layout="wide")
# st.title("Anime Recommender System")

# @st.cache_resource
# def init_pipeline():
#     return AnimeRecommendationPipeline()

# pipeline = init_pipeline()
# query = st.text_input("Enter your anime preferences: eg. light hearted anime with school setting")
# if query:
#     with st.spinner("Fetching recommendations..."):
#         try:
#             recommendations = pipeline.recommend(query)
#             st.subheader("Recommended Anime:")
#             # st.markdown("### Recommendations:")
#             st.write(recommendations)
#         except Exception as e:
#             st.error(f"Error generating recommendations: {e}")

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommnder",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)


