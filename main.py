import os

from dotenv import load_dotenv

import image_config
from fetch_spacex_images import fetch_spacex_launch
from get_nasa_day_images import download_days_pictures
from get_epic_photos import download_epic_photo


def main():
    load_dotenv()
    nasa_token = os.environ['API_NASA_TOKEN']
    image_config.create_directory(image_config.DIRECTORY)
    fetch_spacex_launch()
    download_days_pictures(nasa_token)
    download_epic_photo(nasa_token)


if __name__ == "__main__":
    main()
