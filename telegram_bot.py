import os
import argparse

from dotenv import load_dotenv
import telegram


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = "@SpaceWezhbicka"
    # bot.send_message(text='The Space is well!', chat_id=chat_id)
    bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_0.jpg', 'rb'))
