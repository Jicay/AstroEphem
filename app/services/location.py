import os
import requests


MAP_KEY = os.environ['MAP_KEY']


def get_location(lat, lon):
    url = 'https://geocoder.tilehosting.com/r/' + str(lon) + '/' + str(lat) + '.js?key=' + MAP_KEY
    response = requests.get(url)

    return response.json()
