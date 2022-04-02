from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
bot = Bot(token='')
dp = Dispatcher(bot)

"""Кнопки"""
b1 = KeyboardButton("/ПГУТИ")
b2 = KeyboardButton("/авторы")
b3 = KeyboardButton("/ссылки")
b4 = KeyboardButton('/число')
b5 = KeyboardButton('/команды')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_client.insert(b5).add(b4).add(b3).add(b2).insert(b1)

"""Кнопка ссылка"""
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='VK1 💙', url="https://vk.com/rustamzar")
urlButton2 = InlineKeyboardButton(text='VK2 💙', url="https://vk.com/nojvspine_orig")
urlkb.add(urlButton, urlButton2)

coms = ['start', 'старт', 'links', 'ссылки', 'ПГУТИ', 'пгути', 'автор', 'авторы', 'число']
s = ('\n'.join(f'/{i}' for i in coms))
replys = {"/start" : ['Бззз, привет 🐝\nНапиши мне сообщение, чтобы я его повторил.\nИли воспользуйся командами.', kb_client], 
    '/старт' : ['Бззз, привет 🐝\nНапиши мне сообщение, чтобы я его повторил.\nИли воспользуйся командами.', kb_client], 
    "/links" : ["Ссылки на вк:", urlkb], 
    "/ссылки" : ["Ссылки на вк:", urlkb], 
    "/ПГУТИ" : ['Корпус №1: ул. Л. Толстого, 23 🎓\nКорпус №2: Московское шоссе, 77 🎓', None],
    '/пгути' : ['Корпус №1: ул. Л. Толстого, 23 🎓\nКорпус №2: Московское шоссе, 77 🎓', None], 
    "/автор" : ['Антон 🤝 сосед Антона', None],
    '/авторы' : ['Антон 🤝 сосед Антона', None],
    '/число' : [f'Вот мое число: {randint(1, 100)} 🎲', None],
    '/команды' : [f'Вот список команд:\n{s}', None]}

sticks = {"/start" : 'CAACAgIAAxkBAAEEWZ5iSCWIz5EjcYDtab0E93LIr5jMMwACpwQAAs9fiwfuK3V_8IhGWCME',
    '/старт' : 'CAACAgIAAxkBAAEEWZ5iSCWIz5EjcYDtab0E93LIr5jMMwACpwQAAs9fiwfuK3V_8IhGWCME',
    '/links' : 'CAACAgIAAxkBAAEEWapiSC6nft-yA_MnXwoTdzMzryzZ-wACkwQAAs9fiwfF5YDTXLzqRCME',
    '/ссылки' : 'CAACAgIAAxkBAAEEWapiSC6nft-yA_MnXwoTdzMzryzZ-wACkwQAAs9fiwfF5YDTXLzqRCME',
    '/ПГУТИ' : 'CAACAgIAAxkBAAEEWaxiSC7R5M_tzbpeEXVjf0dXNj-nugACjwQAAs9fiwcjGSIznEAhkCME',
    '/пгути' : 'CAACAgIAAxkBAAEEWaxiSC7R5M_tzbpeEXVjf0dXNj-nugACjwQAAs9fiwcjGSIznEAhkCME',
    '/автор' : 'CAACAgIAAxkBAAEEWahiSC55YSJDahZWYvkX4hcipXR5kAACpgQAAs9fiwcyOrb59JTzZyME',
    '/авторы' : 'CAACAgIAAxkBAAEEWahiSC55YSJDahZWYvkX4hcipXR5kAACpgQAAs9fiwcyOrb59JTzZyME',
    '/число' : 'CAACAgIAAxkBAAEEWbdiSDD-lFBuq5HVMog2BDE7u5CkPAACmwQAAs9fiwfgYldEfWv7oSME'}
""""Команды"""
@dp.message_handler(commands=coms)
async def command_handler(message : types.Message):
    replys['/число'] = [f'Вот мое число: {randint(1, 100)} 🎲', None]
    if message.chat.id != None:
        await bot.send_message(message.chat.id, replys[message.text][0], reply_markup=replys[message.text][1])
        await bot.send_sticker(message.chat.id, rf'{sticks[message.text]}')
    elif message.from_user.id != None:
        await bot.send_message(message.from_user.id, replys[message.text][0], reply_markup=replys[message.text][1])
        await bot.send_sticker(message.from_user.id, rf'{sticks[message.text]}')

@dp.message_handler(commands=['команды'])
async def commands(message : types.Message):
    if message.chat.id != None:
        await bot.send_message(message.chat.id, replys[message.text][0], reply_markup=replys[message.text][1])
    elif message.from_user.id != None:
        await bot.send_message(message.from_user.id, replys[message.text][0], reply_markup=replys[message.text][1])

@dp.message_handler()
async def echo_send(message : types.Message):
    await message.reply(message.text)
    await bot.send_message(message.from_user.id,"🖊️")

executor.start_polling(dp, skip_updates=True)
