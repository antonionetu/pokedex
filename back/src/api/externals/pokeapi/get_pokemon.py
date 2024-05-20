import requests
from .constants import API_URL

def get_pokemon(pokemon_name: str) -> dict:
    """
    Retrieves information about a specific Pokémon.

    Parameters:
    pokemon_name (str): The name of the Pokémon to look up.

    Returns:
    dict: A dictionary containing the Pokémon's information.
    """
    response = requests.get(f'{API_URL}/pokemon/{pokemon_name}')
    return response.json()
