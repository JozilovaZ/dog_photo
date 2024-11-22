import logging
import requests
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = "7597111712:AAGVuflpXHA7BbFpLe6TwU5WTz1HiFYCjNc"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# start komanda uchun handler
@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    username = message.from_user.full_name
    text = f"Assalomu Alaykum {username}\n\n"
    text += f" xush kelibsiz!"
    await message.answer(text, parse_mode="Markdown")


# Rasm chiqaruvchi handler
@dp.message_handler(commands="dog")
async def dog_image(message: types.Message):
    request = requests.get("https://dog.ceo/api/breeds/image/random")
    response = request.json()

    dogg = response['message']
    await message.answer_photo(photo=dogg)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
