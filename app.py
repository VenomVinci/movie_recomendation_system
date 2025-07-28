# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# def fetch_poster(movie_id):
#     requests.get("")

# def recomend(movie):
#     movie_index= movies[movies["title"]== movie].index[0]
#     distances= similarity[movie_index]
#     movies_list =sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]

#     recommended_movies =[]
#     for i in movies_list:
#         movie_id = i[0]
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies 
    



# movies_dict= pickle.load(open("movie_dict.pkl", "rb"))
# movies = pd.DataFrame(movies_dict)                                        

# similarity = pickle.load(open("similarity.pkl", "rb"))


# st.title("Movie Recomending system")

# selected_movie_name = st.selectbox("how do you like to be connected? ",movies["title"].values)

# if st.button("recomend"):
#     recomendations = recomend(selected_movie_name)
#     for i in recomendations:
#       st.write(i)

# import streamlit as st
# import pickle
# import requests
# import pandas as pd


# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters


# st.header('Movie Recommender System')
# movies = pickle.load(open('movie_dict.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])






import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    filtered = movies[movies['title'].str.lower() == movie.lower()]
    if filtered.empty:
        st.error(f"Movie '{movie}' not found!")
        return [], []

    index = filtered.index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])

    recommended_names = []
    recommended_posters = []

    for i in distances[1:6]:
        title = movies.iloc[i[0]]['title']
        recommended_names.append(title)
        recommended_posters.append("https://via.placeholder.com/500x750?text=No+Poster")

    return recommended_names, recommended_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎥 Movie Recommender")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)
    if names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            col.text(names[idx])
            col.image(posters[idx])
