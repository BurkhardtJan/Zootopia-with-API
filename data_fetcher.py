import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    REQUEST_URL = "https://api.api-ninjas.com/v1/animals"
    data = {
        "name": animal_name,
        "X-Api-Key": API_KEY
    }
    response = requests.get(REQUEST_URL, params=data)
    print(response.status_code)
    return response.json()
