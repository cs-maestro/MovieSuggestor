from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(provided_movies, movies_df):
    # Filter movies based on the user's provided movies
    similar_movies_df = movies_df[movies_df['title'].isin(provided_movies)]

    # Calculate cosine similarity between the user's provided movies and all movies
    movie_features = similar_movies_df.iloc[:, 3:]  # Exclude non-feature columns (e.g., title)
    similarity_scores = cosine_similarity(movie_features, movies_df.iloc[:, 3:])

    # Get similar movies based on similarity scores
    similar_movies_indices = similarity_scores.argsort()[0][::-1]  # Descending order
    similar_movies = movies_df.loc[similar_movies_indices, 'title'].tolist()

    return similar_movies