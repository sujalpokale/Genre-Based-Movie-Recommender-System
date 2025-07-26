import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

movies = pd.read_csv('./movies.csv')
movies['processed_genres'] = movies['genres'].str.replace('|',' ' , regex=False)


vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies['processed_genres'])
genre_df = pd.DataFrame(genre_matrix.toarray(),columns=vectorizer.get_feature_names_out())

def recommed_movies_by_genre(input_genres):
  input_genre = input_genres.lower()
  if input_genre not in genre_df.columns:
    return ["Genre not found. Try genres like Action, Comedy,Horror, ect."]
  top_indices = genre_df.sort_values(by = input_genre, ascending=False).head(5).index
  return movies.loc[top_indices,'title'].tolist()

st.title("🎬 Genre-Based Movie Recommender")
genre = st.text_input("Enter a Movie genre (eg. Action, Comedy, Horror):")

if st.button("Get Recommendations"):
  recommendations = recommed_movies_by_genre(genre)
  st.subheader("Recommended Movies:")
  for i , movie in enumerate(recommendations,1):
    st.write(f"{i}. {movie}")