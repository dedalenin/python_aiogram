from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import random

BOT_TOKEN = '7631068222:AAGun7-RCWP21wPCO1uMSoSROvSQVd9ezuE'  # Токен бота

bot = Bot(token=BOT_TOKEN)  #
dp = Dispatcher()

ATTEMPTS = 5

user = {}


def get_ran_number():
    return random.randint(1, 100)


@dp.message(CommandStart())  # обработчик команды start
async def process_start_command(message: Message):
    if (message.from_user.id not in user):  # проверка на наличие пользователя в словаре
        user[message.from_user.id] = {  # добавление пользователя в словарь
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
        }
    await message.answer('Привет!\nДавайте сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help'
                         '\nчтобы начать игру нажми /start_game')


@dp.message(Command(commands='help'))  # обработчик команды help
async def process_help_command(message: Message):
    await message.answer(  # ответ на команду help
        'Правила игры:\n\nЯ загадываю число от 1 до 100, '
        f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
        'попыток\n\nДоступные команды:\n/help - правила '
        'игры и список команд\n/cancel - выйти из игры\n'
        '/stat - посмотреть статистику\n\nДавай сыграем?'
    )


@dp.message(Command(commands='stat'))  # обработчик команды stat
async def process_stat_command(message: Message):
    await message.answer(
        f'your stat: games {user[message.from_user.id]["total_games"]} \n\n wins {user[message.from_user.id]["wins"]} ')  # ответ на команду stat


@dp.message(Command(commands='cancel'))  # обработчик команды cancel
async def process_cancel_command(message: Message):
    if user[message.from_user.id]['in_game']:
        user[message.from_user.id]['in_game'] = False
        await message.answer('Вы вышли из игры, отсосите')
    else:
        await message.answer('Ты больной - мы не играем')


@dp.message(Command(commands='start_game'))  # обработчик команды start_game
async def process_start_game(message: Message):
    if (user[message.from_user.id]['in_game'] != True):
        user[message.from_user.id]['in_game'] = True
        user[message.from_user.id]['attempts'] = ATTEMPTS
        user[message.from_user.id]['secret_number'] = get_ran_number()
        user[message.from_user.id]['total_games'] += 1
        await message.answer('Я загадал, отгадывай')
    else:
        await message.answer('Для начала попробуй выйти /canel(нажми) ')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(
    x.text) <= 100)  # обработчик чисел lambda нужен для того чтобы не писать много кода(вместо if)
async def process_number_answers(message: Message):
    if (user[message.from_user.id]['in_game']):
        if (int(message.text)) == user[message.from_user.id]['secret_number']:
            user[message.from_user.id]['wins'] += 1
            user[message.from_user.id]['in_game'] = False
            await message.answer('Ты выйграл! Мое почтение'
                                 '\nчтобы начать игру нажми /start_game'
                                 )
        elif (user[message.from_user.id]['attempts'] == 1):
            user['in_game'] = False
            await message.answer('Сорри, ты отсосал'
                                 '\nчтобы начать игру нажми /start_game'
                                 )

        elif (int(message.text) < user[message.from_user.id]['secret_number']):
            user[message.from_user.id]['attempts'] -= 1
            await message.answer('Возьми повыше')
        elif (int(message.text) > user[message.from_user.id]['secret_number']):
            user[message.from_user.id]['attempts'] -= 1
            await message.answer('Возьми пониже')
    else:
        await message.answer("Мы еще не играем бро /start_game")


@dp.message()
async def process_other_answers(message: Message):
    if user[message.from_user.id]['in_game']:
        await message.answer(
            'Мы же сейчас с вами играем. '
            'Присылайте, пожалуйста, числа от 1 до 100'
        )
    else:
        await message.answer(
            'Я довольно ограниченный бот, давайте '
            'просто сыграем в игру?'
        )


if __name__ == '__main__':  # запуск бота
    dp.run_polling(bot)  # запуск бота
