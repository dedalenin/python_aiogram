from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import random

BOT_TOKEN = ''  # Токен бота

bot = Bot(token=BOT_TOKEN)  #
dp = Dispatcher()

ATTEMPTS = 5

user = {}


def get_ran_number():
    return random.randint(1, 100)


def chec_on_start(message: Message) -> bool: # Примитивный фильтр для диспетчера
    return message.text == '/start'


@dp.message(chec_on_start) # Применение фильтра для диспетчера
async def ok(message: Message) -> None:
    await message.answer(text='ok start')


if __name__ == '__main__':  # запуск бота
    dp.run_polling(bot)  # запуск бота
