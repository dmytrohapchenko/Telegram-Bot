from bs4 import BeautifulSoup
import requests
from aiogram import types, executor, Dispatcher, Bot
import time



TOKEN = "5885201860:AAGH3wmIZJdNbiqPP4quZ9zp8RLsHbKdaWQ"

PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def msg_start(message: types.Message):
    await bot.send_message(
        message.chat.id, "Hi, if you want to see all news send me /news24"
    )


@dp.message_handler(commands=["news24"])
async def msg_news24(message):
    temp_list = []
    while True:
        r = requests.get("https://24tv.ua/golovni-novini_tag1792/").text
        soup = BeautifulSoup(r, "lxml")
        post = soup.find("app-news-item")
        pub_time = post.find("span").text

        url = post.find("a").get("href")

        if url not in temp_list:
            await bot.send_message(message.chat.id, url)
            await bot.send_message(message.chat.id, pub_time)
            temp_list.append(url)

        time.sleep(10)


if __name__ == "__main__":
    executor.start_polling(dp)
