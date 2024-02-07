import random
from time import sleep

from jikanpy import Jikan

jikan = Jikan()


def progress_bar(progress, total):
    bar_length = 40
    progress_percent = progress / total
    filled_length = int(bar_length * progress_percent)

    bar = f"[{'=' * filled_length}{' ' * (bar_length - filled_length)}] {int(progress_percent * 100)}%"
    print(f"\r{bar}", end='', flush=True)


def get_valid_year(prompt, min_year, max_year):
    while True:
        try:
            value = int(input(prompt))
            if min_year <= value <= max_year:
                return value
            else:
                print(f"Please enter a year between {min_year} and {max_year}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_username(prompt):
    username = input(prompt)
    if username == '':
        return None
    else:
        return username


def get_valid_type():
    while True:
        media_type = input("TV or Movie?: ")
        if media_type == "movie" or media_type == "Movie":
            return "movie"
        if media_type == "TV" or media_type == "tv":
            return "tv"
        else:
            print("Invalid Type!")


def get_all_genres():
    genres_data = jikan.genres('anime')
    genres = genres_data.get('data', [])
    return [ge['name'] for ge in genres]


def get_valid_genre(all_genres):
    while True:
        ge = input("Enter the genre: ")
        if ge in all_genres:
            return ge
        else:
            print("Invalid genre. Please choose from the list.")


def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 1 <= value <= 10:
                return value
            else:
                print("Invalid input. Please enter a number between 1 and 10")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def anime_rec(genre, min_score, num_anime, anime_type, start_year, end_year):
    try:
        filtered_results = []
        anime_list = []
        seasons = ['spring', 'summer', 'winter', 'fall']

        total_iterations = (end_year - start_year + 1) * len(seasons)
        current_iteration = 0

        for year in range(start_year, end_year + 1):
            for s in seasons:
                current_iteration += 1
                progress_bar(current_iteration, total_iterations)

                anime_season = jikan.seasons(year=year, season=s,
                                             parameters={'filter': anime_type})['data']
                anime_list.append(anime_season)
                sleep(0.8)

        print("\n")  # Move to the next line after the progress bar

        for anime in anime_list:
            for an in anime:
                an_genre = an['genres']
                an_demographics = an['demographics']
                an_themes = an['themes']
                an_score = an['score']
                if an_score is not None and (
                        any(ge['name'] == genre for ge in an_genre) or
                        any(theme['name'] == genre for theme in an_themes) or
                        any(demo['name'] == genre for demo in an_demographics)
                ) and an_score >= min_score:
                    filtered_results.append(an)

        random.shuffle(filtered_results)
        selected_shows = filtered_results[:num_anime]
        return selected_shows
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    all_genres = get_all_genres()
    print("All possible genres:")
    print("\n".join(all_genres))

    genre = get_valid_genre(all_genres)
    min_score = get_valid_float_input("Enter the minimum score: ")
    num_anime = get_valid_int_input("Enter the amount of shows to recommend: ")
    a_type = get_valid_type()
    start_year = get_valid_year("Enter the starting year for the search of anime (1980-2024): ", 1980, 2024)
    end_year = get_valid_year("Enter the ending year for the search of anime (1980-2024): ", start_year, 2024)

    recommended_anime = anime_rec(genre, min_score, num_anime, a_type, start_year, end_year)

    if not recommended_anime:
        print(f"No anime found for the genre: {genre}. Please try another genre.")
    else:
        print("\nRecommended Anime:")
        for anime in recommended_anime:
            print(f"Title: {anime['title']}")
            print(f"Score: {anime.get('score', 'N/A')}")
            print(f"Season: {anime.get('season', 'N/A')}" if 'season' in anime else "Season: N/A")
            print(f"Year: {anime.get('year', 'N/A')}")
            print(f"Genre: {anime.get('genre', 'N')}")
            print(f"URL: {anime.get('url', 'N/A')}")
            print("-" * 30)
    print("\nAnime recommendations have been successfully generated!")
    input("Press Enter to close this program.")
