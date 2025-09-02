import requests

def get_tmdb_info(movie_title):
    api_key = 'sua_api_keuy_aqui'  # Substitua pela sua chave de API do TMDB
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    return data['results'] if data['results'] else None

info = get_tmdb_info("O Poderoso Chefão")
print(info)
