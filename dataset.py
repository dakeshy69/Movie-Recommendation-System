from tmdbv3api import TMDb, Movie
import pandas as pd
import time

API_KEY = "064887878002ecfa3edec8ab2ab6ed8d"
NUM_MOVIES = 1000
OUTPUT_FILE = "movies.csv"

tmdb = TMDb()
tmdb.api_key = API_KEY
tmdb.language = 'en'

movie_api = Movie()
movies_list = []
page = 1

while len(movies_list) < NUM_MOVIES:
    popular_movies = movie_api.popular(page=page)
    for m in popular_movies:
        try:
            print(f"Fetching movie ID {m.id} ({len(movies_list)+1}/{NUM_MOVIES})")

            # Fetch full details
            details = movie_api.details(m.id)

            # Fetch credits
            credits = movie_api.credits(m.id)
            cast_list = [c.name for c in list(credits.cast)[:5]] if credits.cast else []
            directors = [c.name for c in list(credits.crew) if c.job == 'Director']
            director_name = directors[0] if directors else None

            movies_list.append({
                'id': details.id,
                'title': details.title,
                'genres': ', '.join([g.name for g in details.genres]) if details.genres else None,
                'overview': details.overview,
                'cast': ', '.join(cast_list) if cast_list else None,
                'director': director_name,
                'release_date': details.release_date,
                'popularity': details.popularity,
                'vote_average': details.vote_average,
                'vote_count': details.vote_count,
                'poster_url': f"https://image.tmdb.org/t/p/w500{details.poster_path}" if details.poster_path else None
            })

            print(f"Extracted {len(movies_list)} / {NUM_MOVIES} movies")

            if len(movies_list) >= NUM_MOVIES:
                break

            time.sleep(0.25)  # small delay to prevent rate limit

        except Exception as e:
            print(f"Skipped movie ID {m.id} due to error: {e}")
            continue

    page += 1

df_movies = pd.DataFrame(movies_list)
df_movies.to_csv(OUTPUT_FILE, index=False)
print(f"Movies CSV created successfully! Total movies: {len(df_movies)}")