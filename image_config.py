import os
from urllib.parse import urlsplit

import requests


DIRECTORY = "images"


def get_image_extension(image_url):
    image_path = urlsplit(image_url).path
    extension = os.path.splitext(image_path)[1]
    return extension


def create_directory():
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)
