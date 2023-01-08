import os
import random
import argparse

import telegram
from dotenv import load_dotenv

import image_config


def send_image(image, chat_id):
    with open(os.path.join(image_config.DIRECTORY, image), 'rb') as file:
        bot.send_document(
            chat_id=chat_id,
            document=file
        )


def select_photo(file_name):
    images = os.listdir(image_config.DIRECTORY)
    image = random.choice(images) if not file_name else file_name    
    return image


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(description='Программа отправляет фотографию из папки images')
    parser.add_argument(
        '-n',
        '--file_name',
        help='Имя файла, который нужно отправить',
        default=''
    )
    args = parser.parse_args()
    image = select_photo(args.file_name)
    send_image(image, chat_id)
