# Создать телеграмм бота желательно сложнее чем калькулятор. Проявите свою фантазию и сделайте что-то интересное)

# Фантазия кончилась :( и я сделал вывод инфы с вики
# PS: В будущем возможно доведу до нормального вида (больший функционал)

import config
from lesson10.homework import wiki
from quotes import Quotes

import logging
from aiogram import Bot, Dispatcher, executor, types

command = [
    {
        'cmd': '/start',
        'desc': 'для запуска'
    },
    {
        'cmd': '{word}',
        'desc': 'для вывода статьи с WIKI'
    },
    {
        'cmd': '/q',
        'desc': 'для вывода рандомной цитаты',
        'btn': 'Цитата'
    },
    {
        'cmd': '/help',
        'desc': 'для вывода списка команд',
        'btn': 'Помощь'
    },
]
commands = lambda: f'Доступные команды:\n\n' + '\n'.join([
    f'{item["cmd"]} - {item["desc"]}'
    for item in command
])
qts = Quotes()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(commands())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    msg = 'Нажми:'
    for item in command:
        try:
            markup.add(types.KeyboardButton(item['btn']))
            msg += f'\n"{item["btn"]}" {item["desc"]}'
        except KeyError:
            pass
    await bot.send_message(message.chat.id, msg, reply_markup=markup)


@dp.message_handler(commands=['q'])
async def send_quotes(message: types.Message):
    q = qts.rand()
    await bot.send_message(message.from_user.id, f'{q["text"]}\n\n- {q["author"]}')


@dp.message_handler(regexp='/info (.*?)')
async def send_info(message: types.Message):
    await message.answer(wiki.getInfo(message.text[5:]))


@dp.message_handler()
async def echo(message: types.Message):
    cmd = message.text.strip()
    q = lambda x: f'{x["text"]}\n\n- {x["author"]}'
    mess = {
        'Цитата': q(qts.rand()),
        'Помощь': commands(),
    }
    try:
        await bot.send_message(message.from_user.id, mess[cmd])
    except KeyError:
        await message.answer(wiki.getInfo(cmd))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
