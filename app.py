import streamlit as st
import pickle

# Load preprocessed data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Custom CSS for red UI
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff0000 0%, #8b0000 100%);
    color: white;
}
.stTitle {
    color: #ffffff;
    font-family: 'Arial Black', sans-serif;
    text-align: center;
}
.stSubheader {
    color: #ffcccc;
    font-size: 24px;
}
.stButton>button {
    background-color: #dc143c;
    color: white;
    border-radius: 10px;
    font-size: 18px;
    padding: 10px 20px;
}
.stSelectbox>div>div>input {
    border-radius: 10px;
    border: 2px solid #ffffff;
}
.stSlider>div>div>div {
    background-color: #dc143c;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get recommendations based on content similarity, including release year and IMDB rating.")

selected_movie = st.selectbox("Select movie from dropdown", movies_list)

num_recommendations = st.slider("Number of recommendations", 1, 10, 5)

def recommend(movie, num):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_ratings = []
    scores = []
    years = []
    for i in distances[1:num+1]:  # Top num similar movies
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_ratings.append(movies.iloc[i[0]].vote_average)
        scores.append(i[1])
        year = movies.iloc[i[0]].release_date.split('-')[0] if movies.iloc[i[0]].release_date else 'N/A'
        years.append(year)
    return recommended_movies, recommended_ratings, scores, years

if st.button("🚀 Get Recommendations"):
    if selected_movie:
        recommendations, ratings, scores, years = recommend(selected_movie, num_recommendations)
        st.subheader(f"🍿 Movies similar to '{selected_movie}':")
        for i, (movie, rating, score, year) in enumerate(zip(recommendations, ratings, scores, years), 1):
            st.write(f"🎞️ {i}. **{movie}** ({year}) - IMDB Rating: {rating}/10, Relevance: {score*5:.1f}/5")
    else:
        st.warning("Please select a movie first.")
