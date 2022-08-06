import argparse

import requests

import image_config


def get_id():
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинки запуска ракет space X'
    )
    parser.add_argument('-id', '--id', help='id запуска', default="latest")
    args = parser.parse_args()
    return args.id


def fetch_spacex_launch():
    id = get_id()
    image_url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(image_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']
    for num, link in enumerate(images_links):
        filename = f'spacex_{num}.jpeg'
        image_config.download_image(link, f"{image_config.DIRECTORY}/{filename}")


if __name__ == '__main__':
    image_config.create_directory()
    parser = argparse.ArgumentParser(description='Программа скачивает фотографии с запуска ракет от компании SpaceX')
    parser.add_argument('-id', '--id', help='ID запуска')
    args = parser.parse_args()
    fetch_spacex_launch(args.id)
