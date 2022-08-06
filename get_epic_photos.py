import requests
import datetime

import for_image


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
        image_datetime = datetime.datetime.fromisoformat(image['date'])
        image_date = image_datetime.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
        response = requests.get(url, params=params)
        response.raise_for_status()
        image_url = response.url
        filename = f'epic_{index}.png'
        download_path = f"{for_image.DIRECTORY}/{filename}"
        for_image.download_image(image_url, download_path)
