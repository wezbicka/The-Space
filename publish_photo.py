import os
import random
import argparse

import telegram
from dotenv import load_dotenv

import image_config


TG_TOKEN = os.environ['TG_TOKEN']
CHAT_ID = os.getenv("CHAT_ID")
bot = telegram.Bot(token=TG_TOKEN)


def send_photo(file_name):
    if file_name == '':
        image = random.choice(image_config.DIRECTORY)
        with open(os.path.join(image_config.DIRECTORY, image), 'rb') as file:
            bot.send_document(
                chat_id=CHAT_ID,
                document=file
            )
    else:
        bot.send_document(
            chat_id=CHAT_ID,
            document=open(os.path.join(image_config.DIRECTORY, file_name), 'rb')
        )


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Программа отправляет фотографию из папки images')
    parser.add_argument(
        '-n',
        '--file_name',
        help='Имя файла, который нужно отправить',
        default=''
    )
    args = parser.parse_args()
    send_photo(args.file_name)
