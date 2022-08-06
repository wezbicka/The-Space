import requests

import for_image


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
        ext = for_image.get_image_extension(image_url)
        filename = f'nasa_apod_{index}{ext}'
        download_path = f"{for_image.DIRECTORY}/{filename}"
        for_image.download_image(image_url, download_path)
