# Anime Reccomandation App
Anime Recommendation Python Script Documentation
This document provides an overview of the Python script for recommending anime based on user-specified criteria.

Functionality
The script allows users to search for anime recommendations based on the following criteria:

Genre: Select a genre from a list of available options.
Minimum score: Specify the minimum score threshold for recommendations.
Number of recommendations: Choose the desired number of anime recommendations.
Anime type: Select between TV shows, movies, OVAs, or ONAs.
Start and end year: Define the search range for anime release years.
Usage
Run the script: Execute the script using a Python interpreter.
Genre selection: Choose a genre from the displayed list.
Minimum score: Enter the minimum score you prefer for recommendations (between 1 and 10).
Number of recommendations: Specify the desired number of recommended anime.
Anime type: Select the type of anime you're interested in (TV, Movie, OVA, or ONA).
Start and end year: Enter the starting and ending years for the anime search range (between 1980 and 2024).
The script will display the recommended anime along with details like title, score, season (if applicable), year, genres, demographics, themes, and URL.

Script Breakdown
jikanpy library: The script utilizes the jikanpy library to interact with the Jikan API, retrieving anime information.
get_all_genres function: Retrieves a list of all available anime genres from the Jikan API.
get_valid_genre function: Ensures the user selects a valid genre from the available list.
get_valid_float_input function: Validates user input for the minimum score, ensuring it's between 1 and 10.
get_valid_int_input function: Validates user input for the number of recommendations and ensures it's a positive integer.
get_valid_type function: Ensures the user selects a valid anime type (TV, Movie, OVA, or ONA).
get_valid_year function: Validates user input for start and end years, ensuring they are within the specified range (1980-2024).
anime_rec function: The core function that performs the anime recommendation logic:
Iterates through anime data based on the specified criteria.
Filters anime based on genre, score, anime type, and release year.
Randomly selects the desired number of recommendations from the filtered results.
Progress bar: A progress bar is displayed during the anime search process to provide feedback to the user.
Additional Notes
The script relies on an active internet connection to access the Jikan API.
