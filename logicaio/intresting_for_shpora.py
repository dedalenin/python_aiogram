from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import random
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated


BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
@dp.message(F.content_type.in_({'voice', 'video', 'text'}))
async def process_send_vovite(message: Message):
    await message.answer(text='Вы прислали войс, видео или текст')

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')

@dp.message(F.from_user.id.in_({193905674, 173901673, 144941561})) # РЕализация админ меню через F.
async def admin_menu(message: Message):
    await message.answer(text='Вы админ!')
