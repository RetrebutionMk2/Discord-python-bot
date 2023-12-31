from utils.keep_alive import keep_alive
from utils.bot import Bot
import os


def main():
    bot = Bot()
    TOKEN = os.environ.get("TOKEN")
    keep_alive()
    bot.run(TOKEN)

if __name__=="__main__":
    main()