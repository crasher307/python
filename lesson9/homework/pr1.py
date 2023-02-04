# Создайте любую программу .py при помощи виртуального окружения и PIP.
# Отправьте репозиторий, где будет этот файл и файл requirements.txt
#
# 2. Создайте любого бота телеграмм(можно самый простой), главное чтобы у вас к след. уроку был свой бот в телеграмме,
# в нем вы сможете работать над созданием нового бота на 10 семинаре.

import config
from quotes import Quotes

import logging
from aiogram import Bot, Dispatcher, executor, types

command = [
    {'cmd': '/help', 'desc': 'Вывод списка команд'},
    {'cmd': '/q', 'desc': 'Вывод рандомной цитаты'}
]
qts = Quotes()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        f'Привет, доступные команды:\n\n' +
        '\n'.join([f'{item["cmd"]}\t- {item["desc"]}' for item in command])
    )


@dp.message_handler(commands=['q'])
async def quotes(message: types.Message):
    q = qts.rand()
    msg = f'{q["text"]}\n\n- {q["author"]}'
    # await message.reply(msg)
    await bot.send_message(message.from_user.id, msg)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    # await message.answer(message.text)
    await message.answer(
        f'Доступные команды:\n\n' +
        '\n'.join([f'{item["cmd"]}\t- {item["desc"]}' for item in command])
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
