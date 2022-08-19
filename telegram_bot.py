import os
from time import sleep
import argparse
import random

from dotenv import load_dotenv
import telegram

from image_config import DIRECTORY
from publish_photo import send_image

def get_wait_time():
    parser = argparse.ArgumentParser(
        description='Бесконечно отправляет все фотографии из папки с задержкой'
    )
    parser.add_argument(
        '-t',
        '--wait_time',
        help='время задержки',
        type=int,
        default=os.getenv('WAIT_TIME', 14400)
    )
    args = parser.parse_args()
    return args.wait_time


def send_photos(wait_time, chat_id):
    images = os.listdir(DIRECTORY)
    while True:
        try:
            for image in images:
                send_image(image, chat_id)
                sleep(wait_time)
            random.shuffle(images)
        except telegram.error.NetworkError:
            sleep(2)


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = os.environ["TG_CHAT_ID"]
    wait_time = get_wait_time()
    send_photos(wait_time, chat_id)
