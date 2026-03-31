import pandas as pd
import numpy as np
import random

NUM_USERS = 100  # number of fake users
MIN_RATINGS_PER_USER = 20  # minimum movies each user rates
MAX_RATINGS_PER_USER = 50  # maximum movies each user rates
MOVIES_FILE = "movies.csv"
OUTPUT_FILE = "ratings.csv"

movies = pd.read_csv(MOVIES_FILE)
movie_ids = movies['id'].tolist()

ratings_list = []

for user_id in range(1, NUM_USERS + 1):

    num_rated_movies = random.randint(MIN_RATINGS_PER_USER, MAX_RATINGS_PER_USER)
    rated_movies = random.sample(movie_ids, num_rated_movies)

    for movie_id in rated_movies:

        movie_row = movies[movies['id'] == movie_id].iloc[0]
        vote_avg = movie_row['vote_average']
        vote_count = movie_row['vote_count']


        rating = np.clip(np.random.normal(loc=vote_avg, scale=1.0), 1, 10)

        ratings_list.append({
            'userId': user_id,
            'movieId': movie_id,
            'rating': round(rating, 1)
        })

df_ratings = pd.DataFrame(ratings_list)
df_ratings.to_csv(OUTPUT_FILE, index=False)

print(f"ratings.csv created successfully! Total ratings: {len(df_ratings)}")