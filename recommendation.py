def generate_recommendations(num_recommended_movies, provided_movies,similar_movies, movies_df):
    recommended_movies = []

    # Select top 5 recommended movies based on similarity
    for movie in similar_movies:
        if movie not in recommended_movies and movie not in provided_movies:
            recommended_movies.append(movie)
        if len(recommended_movies) == num_recommended_movies:
            break

    return recommended_movies