import asyncio
from telegram import Bot

# Your token
my_token = "7759685629:AAF4bRo029QE9A5TtN2eBqXZJcuHIYcF2Nw"
CHAT_ID = 8100078553

async def send_message():
    bot = Bot(token=my_token)
    while True:
        await bot.send_message(chat_id=CHAT_ID, text="Hi, how can I help you?")
        
        await asyncio.sleep(10)

# Run the send_message coroutine
if __name__ == "__main__":
    asyncio.run(send_message()) 