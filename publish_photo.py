import os
import random
import argparse

import telegram
from dotenv import load_dotenv

import image_config


def send_photo(file_name, chat_id):
    images = os.listdir(image_config.DIRECTORY)
    if file_name == '':
        image = random.choice(images)
        with open(os.path.join(image_config.DIRECTORY, image), 'rb') as file:
            bot.send_document(
                chat_id=chat_id,
                document=file
            )
    else:
        bot.send_document(
            chat_id=chat_id,
            document=open(os.path.join(image_config.DIRECTORY, file_name), 'rb')
        )


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
    send_photo(args.file_name, chat_id)
