# Movie Suggestor

Movie Suggestor is a Python-based recommendation system that provides movie recommendations based on user-provided movies. It leverages machine learning techniques and data processing to offer personalized movie suggestions.

## Overview

The Movie Suggestor project aims to assist users in discovering new movies that are similar to their favorite movies. By inputting one or more movie names, the system generates a list of recommended movies using advanced similarity calculations and recommendation algorithms.

## Features

- **Movie Data Processing**: The project preprocesses and cleanses the movie dataset, handling missing values and removing duplicates. It also extracts relevant features such as movie genres.

- **Fuzzy Matching**: The system employs fuzzy matching techniques to handle cases where exact movie titles are not provided. It suggests alternative movie titles based on similarity scores.

- **Cosine Similarity**: Movie similarity is calculated using the cosine similarity measure. This technique compares the features of user-provided movies with the features of all movies in the dataset to determine similarity.

- **Top Movie Recommendations**: Based on the calculated similarity scores, the system generates a list of top recommended movies that are similar to the user-provided movies.

## Technologies Used

- Python: The project is implemented using the Python programming language.

- Libraries:
  - pandas: For data manipulation and preprocessing.
  - fuzzywuzzy: For fuzzy string matching.
  - scikit-learn: For calculating cosine similarity.

## Usage

1. Clone the repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Run the `main.py` file to start the program.
4. Follow the prompts to enter your favorite movie names and the number of recommended movies.
5. The program will display the recommended movies based on your input.

## Dataset

The project uses the [MovieLens dataset](https://grouplens.org/datasets/movielens/) for movie ratings and information. The dataset contains a collection of movies along with user ratings.
