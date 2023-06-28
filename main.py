import data_processing
import similarity_calculation
import recommendation
from fuzzywuzzy import fuzz

# Load and preprocess the dataset
ratings_df, movies_df = data_processing.load_dataset('./Data/')

# Explain the working of program
print("\n\033[1;34m" + "|| MOVIE SUGGESTOR ||".center(80) + "\033[0m")
print("\033[1m\nYou will provide me with one or more movie names, and I will recommend movies to you based on that.\033[0m")
print("\033[1mLet's get started!\n\033[0m")

# Get the number of provided movies from the user
num_provided_movies = int(input("How many movies will you provide me? "))

# Input format
print("\nThe movie names should be in the following format: NAME (YEAR)")

# Collect the provided movie names from the user
provided_movies = []
num_entered_movies = 0

for i in range(num_provided_movies):
    while True:
        movie_name = input(f"\nMovie #{i+1}: ")

        # Check if the movie name exactly matches the titles in the dataset
        if movie_name in movies_df['title'].values:
            provided_movies.append(movie_name)
            num_entered_movies += 1
            break

        # Try to find similar movies using fuzzy matching
        ratio_threshold = 70  # Adjust the threshold as needed
        matches = movies_df['title'].apply(lambda x: fuzz.token_set_ratio(movie_name, x))
        best_match_idx = matches.idxmax()

        if matches[best_match_idx] >= ratio_threshold:
            best_match_title = movies_df.loc[best_match_idx, 'title']
            print(f"Did you mean {best_match_title}?")
            answer = input("Enter Y for Yes, N for No: ")

            if answer.lower() == 'y':
                provided_movies.append(best_match_title)
                num_entered_movies += 1
                break
            else:
                print("Please try again.")
        else:
            print("Please try again.")

    if num_entered_movies == num_provided_movies:
        break

# Calculate movie similarity
similar_movies = similarity_calculation.calculate_similarity(provided_movies, movies_df)

# Get the number of movies to recommend from the user
while True:
    try:
        num_recommended_movies = int(input("\nHow many movies should I recommend (Enter a number between 1 and 10)? "))
        if 1 <= num_recommended_movies <= 10:
            break
        else:
            print("Invalid input. Please enter a whole number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a whole number between 1 and 10.")

# Generate movie recommendations
recommended_movies = recommendation.generate_recommendations(num_recommended_movies, provided_movies, similar_movies, movies_df)

# Display the recommendations
print("\nRecommended Movies:")
for i in range(num_recommended_movies):
    print(f"{i+1}: {recommended_movies[i]}")

print("")
