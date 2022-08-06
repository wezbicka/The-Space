import os
import argparse

from dotenv import load_dotenv
import telegram


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    print(bot.get_me())