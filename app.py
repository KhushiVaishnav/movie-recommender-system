import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    ind = movies.index[movies['title'] == movie][0]
    dist = similarity1[ind]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
# movie_list is basically now our new_df
movies = pd.DataFrame(movies_list)

similarity1 = pickle.load(open('similarity1.pkl', 'rb'))


# Interface
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    st.subheader("🎬 Recommended Movies")

    for movie in recommendations:
        st.write("⭐ " + movie)