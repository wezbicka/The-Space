import os

from dotenv import load_dotenv

import for_image
from fetch_spacex_images import fetch_spacex_last_launch
from get_nasa_day_images import download_days_pictures
from get_epic_photos import download_epic_photo


def main():
    load_dotenv()
    nasa_token = os.environ['API_NASA_TOKEN']
    # filename = 'hubble.jpeg'
    for_image.create_directory(for_image.DIRECTORY)
    # download_path = f"{for_image.DIRECTORY}/{filename}"
    # image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # for_image.download_image(image_url, download_path)
    fetch_spacex_last_launch()
    download_days_pictures(nasa_token)
    download_epic_photo(nasa_token)


if __name__ == "__main__":
    main()
