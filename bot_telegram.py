from telegram import Bot
from telegram.constants import ParseMode
import time

#التوكن الخاص بي
my_token = "7759685629:AAF4bRo029QE9A5TtN2eBqXZJcuHIYcF2Nw"
CHAT_ID = 8100078553

bot = Bot(token=my_token)

#ارسال رساله كل 10 ثواني

while True:
    bot.send_message(chat_id=CHAT_ID, text="This is me")

    time.sleep(10)

