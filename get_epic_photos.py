import datetime
import argparse
import os

import requests
from dotenv import load_dotenv

import image_config


def download_epic_photo(nasa_token, count):
    params = {
        "api_key": nasa_token
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()[:count]
    for index, image in enumerate(images):
        image_name = image['image']
        image_datetime = datetime.datetime.fromisoformat(image['date'])
        image_date = image_datetime.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
        response = requests.get(url, params=params)
        response.raise_for_status()
        image_url = response.url
        filename = f'epic_{index}.png'
        download_path = os.path.join(
            image_config.DIRECTORY,
            filename
        )
        image_config.download_image(image_url, download_path)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['API_NASA_TOKEN']
    image_config.create_directory()
    parser = argparse.ArgumentParser(description='Программа скачивает фото Земли из космоса')
    parser.add_argument('-c', '--count', help='количество', default=10, type=int)
    args = parser.parse_args()
    count = args.count
    download_epic_photo(nasa_token, count) 
