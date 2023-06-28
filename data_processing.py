import pandas as pd

def load_dataset(dataset_path):
    ratings_file = dataset_path + '/ratings.csv'
    movies_file = dataset_path + '/movies.csv'
    ratings_df = pd.read_csv(ratings_file)
    movies_df = pd.read_csv(movies_file)

    # Preprocessing steps
    # Handle missing values
    ratings_df.dropna(inplace=True)

    # Clean data (if needed)
    # Example: Remove duplicates
    ratings_df.drop_duplicates(inplace=True)

    # Feature extraction
    # Extract relevant features for movie similarity and user preference inference
    # Example: Extract movie genres from the 'movies_df' DataFrame
    genres_df = movies_df['genres'].str.get_dummies('|')
    movies_df = pd.concat([movies_df, genres_df], axis=1)

    return ratings_df, movies_df
