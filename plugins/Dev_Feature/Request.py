def ai_spell_check(user_input):
    from fuzzywuzzy import fuzz
    import requests

    # Fetch the top movies from an external API, limiting results to top 10
    response = requests.get('https://api.example.com/top-movies?limit=10')  # Replace with actual API
    top_movies = response.json()

    # Store movie titles in a list for comparison
    movie_titles = [movie['title'] for movie in top_movies]

    # Compare user input against movie titles using token_set_ratio from fuzzywuzzy
    matched_movies = sorted(movie_titles, key=lambda title: fuzz.token_set_ratio(user_input, title), reverse=True)
    # Get the top match 
    top_match = matched_movies[:10]

    return top_match
