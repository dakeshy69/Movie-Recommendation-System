import pandas as pd
import pickle
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#for loading csv files
def load_data(movies_file='movies_cleaned.csv', ratings_file='ratings_cleaned.csv'):
    movies = pd.read_csv(movies_file)
    ratings = pd.read_csv(ratings_file)
    return movies, ratings



