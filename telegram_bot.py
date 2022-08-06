import os
from time import sleep
import argparse
import random

from dotenv import load_dotenv
import telegram

from image_config import DIRECTORY


def get_wait_time():
    parser = argparse.ArgumentParser(
        description='Бесконечно отправляет все фотографии из папки с задержкой'
    )
    parser.add_argument(
        '-t',
        '--wait_time',
        help='время задержки',
        type=int,
        default=os.environ['WAIT_TIME']
    )
    args = parser.parse_args()
    return args.wait_time


def send_photos(wait_time):
    images = os.listdir(DIRECTORY)
    while True:
        try:
            for image in images:
                bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
                sleep(wait_time)
            random.shuffle(images)
        except telegram.error.NetworkError:
            sleep(2)


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = "@SpaceWezhbicka"
    wait_time = get_wait_time()
    send_photos(wait_time)
