import argparse
import os

import requests
from dotenv import load_dotenv

import image_config


def download_days_pictures(nasa_token, count):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": count,
        "api_key": nasa_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()
    for index, day_image in enumerate(images_response):
        if day_image['media_type'] != 'image':
            continue
        image_url = day_image["url"]
        ext = image_config.get_image_extension(image_url)
        filename = f'nasa_apod_{index}{ext}'
        download_path = os.path.join(image_config.DIRECTORY, filename)
        image_config.download_image(image_url, download_path)


if __name__ == '__main__':
    load_dotenv()
    image_config.create_directory()
    nasa_token = os.environ['API_NASA_TOKEN']
    parser = argparse.ArgumentParser(description='Программа скачивает популярные фотографии из космоса')
    parser.add_argument('-c', '--count', help='количество', default=10, type=int)
    args = parser.parse_args()
    count = args.count
    download_days_pictures(nasa_token, count)
