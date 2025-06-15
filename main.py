from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import random

BOT_TOKEN = ''  # Токен бота

bot = Bot(token=BOT_TOKEN)  #
dp = Dispatcher()
admins = []
admins.append()



def check(message: Message) -> bool:
    if (message.from_user.id in admins and message.text == '/admin'):
        return True
    else:
        return False


@dp.message(check)
async def admin_menu(message: Message):
    await message.answer('вы админ! Ура!')


if __name__ == '__main__':  # запуск бота
    dp.run_polling(bot)  # запуск бота
