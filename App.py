import pickle as pk
import streamlit as st

st.header('Movie Recommendation')

movie_dataset = pk.load(open('movie_dataset.pkl','rb'))
similarity = pk.load(open('similarity.pkl','rb'))

def recommend_movie(movie_name):
    movie_index = movie_dataset[movie_dataset['title']==movie_name].index[0]
    similar_movies = sorted(list(enumerate(similarity[movie_index])),reverse=True, key=lambda vector:vector[1])
    recommendations = []

    for i in similar_movies[1:6]:
        recommendations.append(movie_dataset.iloc[i[0]].title + ' with similarity of ' + str(round(i[1]*100,2)))
    return recommendations

selected_movie = st.selectbox('Select Movie/TV Show', movie_dataset['title'])

if st.button('Recommend'):
    result = recommend_movie(selected_movie)

    st.text(result[0])
    st.text(result[1])
    st.text(result[2])
    st.text(result[3])
    st.text(result[4])
