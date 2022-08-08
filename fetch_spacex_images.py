import argparse

import requests

import image_config


def get_id():
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинки запуска ракет space X'
    )
    parser.add_argument('-id', '--launch_id', help='id запуска', default="latest")
    args = parser.parse_args()
    return args.launch_id


def fetch_spacex_launch():
    launch_id = get_id()
    image_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(image_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']
    for num, link in enumerate(images_links):
        filename = f'spacex_{num}.jpeg'
        image_config.py.download_image(link, f"{image_config.py.DIRECTORY}/{filename}")


if __name__ == '__main__':
    image_config.create_directory()
    fetch_spacex_launch()
