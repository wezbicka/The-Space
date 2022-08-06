import argparse

import requests

import for_image


def get_id():
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинки запуска ракет space X'
    )
    parser.add_argument('--id', help='id запуска', default="latest")
    args = parser.parse_args()
    return args.id


def fetch_spacex_last_launch():
    # id = "5eb87d47ffd86e000604b38a"
    id = get_id()
    image_url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(image_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']
    for num, link in enumerate(images_links):
        filename = f'spacex_{num}.jpeg'
        for_image.download_image(link, f"{for_image.DIRECTORY}/{filename}")
