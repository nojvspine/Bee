from aiogram import Bot, types #все нужные импорты
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import logging
import os

TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN) #токен бота
dp = Dispatcher(bot) #!в aiogram команды бота выполняет диспетчер

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

async def on_shutdown(dispatcher):
    await bot.delete_webhook()
"""Кнопка ссылка"""
urlkb = InlineKeyboardMarkup(row_width=1) #инлайн-клавиатура позволяет прикреплять ссылки к сообщениям
urlButton = InlineKeyboardButton(text='VK1 💙', url="https://vk.com/rustamzar")
urlButton2 = InlineKeyboardButton(text='VK2 💙', url="https://vk.com/nojvspine_orig")
urlkb.add(urlButton, urlButton2)

urlkb2 = InlineKeyboardMarkup(row_width=1)
urlButton3 = InlineKeyboardButton(text="Личный кабинет", url="https://portal.psuti.ru/user/sign-in/login")
urlButton4 = InlineKeyboardButton(text="Новости ПГУТИ", url="https://www.psuti.ru/news")
urlButton5 = InlineKeyboardButton(text="Расписание", url="https://www.psuti.ru/ru/students/timetable")
urlButton6 = InlineKeyboardButton(text="Абитуриентам", url="https://www.psuti.ru/ru/abitur")
urlkb2.add(urlButton3, urlButton4, urlButton5, urlButton6)
# список команд бота
coms = ['start', 'старт', 'ПГУТИ', 'psuti', 'authors', 'авторы', 'число', 'randnum']
# словарь ответов бота
replys = {"/start" : ['Бззз, привет 🐝\nНапиши мне сообщение, чтобы я его повторил.\nИли воспользуйся командами.', None, None], 
    '/старт' : ['Бззз, привет 🐝\nНапиши мне сообщение, чтобы я его повторил.\nИли воспользуйся командами.', None, None],
    "/ПГУТИ" : ['Корпус №1: ул. Л. Толстого, 23 🎓\nКорпус №2: Московское шоссе, 77 🎓', urlkb2, [53.22535,50.195459], [53.19225,50.09317]],
    '/psuti' : ['Корпус №1: ул. Л. Толстого, 23 🎓\nКорпус №2: Московское шоссе, 77 🎓', urlkb2, [53.22535,50.195459], [53.19225,50.09317]], 
    "/authors" : ['Антон 🤝 сосед Антона', urlkb, None],
    '/авторы' : ['Антон 🤝 сосед Антона', urlkb, None],
    '/randnum' : [f'Вот мое число: {randint(1, 100)} 🎲', None, None]}
# стикеры, прикрепляемые к ответу
sticks = {"/start" : 4,
    '/старт' : 4,
    '/ПГУТИ' : 9,
    '/psuti' : 9,
    '/authors' : 17,
    '/авторы' : 17,
    '/randnum' : 11,
    '/file' : 16,
    '/video' : 15,
    '/contact' : 5,
    '/audio' : 8}

""""Команды""" # обработчики команд
@dp.message_handler(commands=coms) # оператор @ используется для короткой записи декоратора
# ?декоратор - функция, обрабатывающая другую функцию; он позволяет расширить её функционал без явного изменения функции
async def command_handler(message : types.Message):
    replys['/randnum'] = [f'Вот мое число: {randint(1, 100)} 🎲', None, None]
    s = await bot.get_sticker_set('SweetyBee') # функция получения стикерпака
    text = message.text
    if '@' in text:
        text = text[0:text.find('@')]
    if message.chat.id != None: # бот отправляет сообщение в тот чат, откуда ему написали
        await bot.send_message(message.chat.id, replys[text][0], reply_markup=replys[text][1])
        if(replys[text][2] != None):
            await bot.send_location(message.chat.id, replys[text][2][0], replys[text][2][1])
            await bot.send_location(message.chat.id, replys[text][3][0], replys[text][3][1])
        await bot.send_sticker(message.chat.id, rf'{s.stickers[sticks[text]].file_id}')
    elif message.from_user.id != None:
        await bot.send_message(message.from_user.id, replys[text][0], reply_markup=replys[text][1])
        if(replys[text][2] != None):
            await bot.send_location(message.from_user.id, replys[text][2][0], replys[text][2][1])
            await bot.send_location(message.from_user.id, replys[text][3][0], replys[text][3][1])
        await bot.send_sticker(message.from_user.id, rf'{s.stickers[sticks[text]].file_id}')

@dp.message_handler(commands="file")
async def cm_1(message : types.Message):
    text = message.text
    if '@' in text:
        text = text[0:text.find('@')]
    s = await bot.get_sticker_set('SweetyBee')
    await bot.send_message(message.chat.id, "Файлы к лекции 12 📁")
    await bot.send_document(message.chat.id, document="BQACAgIAAxkBAAIFG2Jq1aUxaEF9Ukzd09wtBzJNRooGAAKNGQACaIdQS5SDUcFkaZ_NJAQ")
    await bot.send_document(message.chat.id, document="BQACAgIAAxkBAAIFGmJq574caihCq27b7qH0mMRhccfeAAKMGQACaIdQSw2dZ6U0RvFOJAQ")
    await bot.send_sticker(message.chat.id, rf'{s.stickers[sticks[text]].file_id}')

@dp.message_handler(commands='video')
async def cm_2(message : types.Message):
    text = message.text
    if '@' in text:
        text = text[0:text.find('@')]
    s = await bot.get_sticker_set('SweetyBee')
    await bot.send_message(message.chat.id, "Видео о ПГУТИ 📹")
    await bot.send_video(message.chat.id, video='BAACAgIAAxkBAAIGG2Jq7PhARob_qzT-DMlj3375-2orAAIcGgACaIdQSxT5o4Esy1vIJAQ')
    await bot.send_sticker(message.chat.id, rf'{s.stickers[sticks[text]].file_id}')

@dp.message_handler(commands='contact')
async def cm_3(message : types.Message):
    text = message.text
    if '@' in text:
        text = text[0:text.find('@')]
    s = await bot.get_sticker_set('SweetyBee')
    await bot.send_contact(message.chat.id, phone_number='+13372281488', first_name="p4elka", last_name="p4el")
    await bot.send_sticker(message.chat.id, rf'{s.stickers[sticks[text]].file_id}')

@dp.message_handler(commands='audio')
async def cm_4(message : types.Message):
    text = message.text
    if '@' in text:
        text = text[0:text.find('@')]
    s = await bot.get_sticker_set('SweetyBee')
    await bot.send_audio(message.chat.id, audio="CQACAgIAAxkBAAIGpGJq95FSVYBGGGCp8sDRgnVVs4UeAAKrFQACaIdYS6t8WjgXUKQ7JAQ")
    await bot.send_sticker(message.chat.id, rf'{s.stickers[sticks[text]].file_id}')

if __name__ == '__main__': # основная функция, запускающая бота, #?наподобие mainloop() при создании GUI
    logging.basicConfig(level=logging.INFO) 
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        )