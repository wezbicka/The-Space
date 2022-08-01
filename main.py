import os
import requests
from urllib.parse import urlsplit
import datetime
from dotenv import load_dotenv
load_dotenv()


DIRECTORY = "images"


def create_directory(DIRECTORY):
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def get_link_list():
    id = "5eb87d47ffd86e000604b38a"
    image_url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(image_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']
    return images_links


def download_days_pictures(nasa_token):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 10,
        "api_key": nasa_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()
    for index, day_image in enumerate(images_response):
        image_url = day_image["url"]
        ext = get_image_extension(image_url)
        filename = f'nasa_apod_{index}{ext}'
        download_path = f"{DIRECTORY}/{filename}"
        download_image(image_url, download_path)


def get_image_extension(image_url):
    image_path = urlsplit(image_url).path
    extension = os.path.splitext(image_path)[1]
    return extension


def fetch_spacex_last_launch(images_links):
    for num, link in enumerate(images_links):
        filename = f'spacex_{num}.jpeg'
        download_image(link, f"{DIRECTORY}/{filename}")


def download_epic_photo(nasa_token):
    params = {
        "api_key": nasa_token
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()[:10]
    for index, image in enumerate(images):
        image_name = image['image']
        image_date = datetime.datetime.fromisoformat(image['date'])
        image_date = image_date.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
        response = requests.get(url, params=params)
        response.raise_for_status()
        image_url = response.url
        filename = f'epic_{index}.png'
        download_path = f"{DIRECTORY}/{filename}"
        download_image(image_url, download_path)


def main():
    nasa_token = os.environ['API_NASA_TOKEN']
    filename = 'hubble.jpeg'
    create_directory(DIRECTORY)
    download_path = f"{DIRECTORY}/{filename}"
    image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_image(image_url, download_path)
    images_links = get_link_list()
    fetch_spacex_last_launch(images_links)
    get_image_extension("https://example.com/txt/hello%20world.txt?v=9#python")
    download_days_pictures(nasa_token)
    download_epic_photo(nasa_token)


if __name__ == "__main__":
    main()
