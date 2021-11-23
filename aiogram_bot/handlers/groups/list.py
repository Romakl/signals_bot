import time

from aiogram import types
from filters.group_filter import ChatIdFilter, IsGroup
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import seminar
from keyboards.inline.choice_buttons import akadembutton, seminar_timer
from loader import dp, bot
from utils.db_api.quick_commands import select_user
from utils.redis.redis_db import redis_get


@dp.message_handler(Command('List'), ChatIdFilter())
async def chat_buttons(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Бот к вашим услугам:", reply_markup=akadembutton)


@dp.message_handler(Command('key'))
async def chat_buttons(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Клавиатура убрана", reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(seminar.filter(item_name='Popko'))
async def get_data(call: CallbackQuery, ):
    redis_value = await redis_get()
    await call.message.answer(f'🕐-----Информация на {redis_value[0]}:{redis_value[1]}-----🕐\n'
                              '☁️------------Погода, Киев-----------☁️\n'
                              f'Температура за окном: {redis_value[2]}°C\n'
                              f'Состояние облаков: {redis_value[3]}\n'
                              f'Влажность: {redis_value[4]}%\n'
                              f'Скорость ветра: {redis_value[5]} КМ/Ч\n'
                              '\n'
                              '💵---------Курс Валют, Киев--------💵\n'
                              f'USD(Черный рынок): {redis_value[6]} - {redis_value[7]}\n'
                              f'EUR(Черный рынок): {redis_value[8]} - {redis_value[9]}\n'
                              f'CHF(Черный рынок): {redis_value[10]} - {redis_value[11]}\n'
                              '\n'
                              '🪙----------------Crypto----------------🪙\n'
                              f'BTC: {redis_value[12]}$\n'
                              f'ETH: {redis_value[13]}$\n'
                              f'SOL: {redis_value[14]}$\n'
                              f'BNB: {redis_value[15]}$')


@dp.callback_query_handler(seminar.filter(item_name='seminar'), IsGroup())
async def timer(call: CallbackQuery):
    time_count = 24
    for i in range(time_count, 0, -1):
        await call.message.edit_text(text=f'Осталось {i * 5} секунд')
        time.sleep(5)
    await call.message.delete()
    await call.message.answer(text="The time has cum", disable_notification=True, reply_markup=seminar_timer)


@dp.callback_query_handler(seminar.filter(item_name='boyz'))
async def buying_pear(call: CallbackQuery):
    await call.message.answer('На данный момент эта функция не реализована, я хочу с вами посоветоваться. Я предлагаю '
                              'для поддержания группы зарезервировать перспективные криптовалюты(Например BNB или '
                              'SOL) или индексы(NASDAQ, SNP500) и выдавать по кусочку за полезные действия для '
                              'группы, так будет стимул помогать друг другу и каждый станет 100% богаче к концу '
                              'обучения. Так же есть пару проектов по типу Instagram бота, который мы разрабатываем '
                              'вместе с нашим Ильёй для просмотра аккаунтов анонимно, скачивания историй и постов, '
                              'накрутка лайков. Если это будет интересно, дайте зелёный свет нам) Так же вы можете '
                              'порекомендовать нам новый проект и мы реализуем его в рамках бота')


@dp.callback_query_handler(seminar.filter(item_name='close'))
async def buying_pear(call: CallbackQuery):
    await call.message.edit_reply_markup()


@dp.message_handler(Command('kek'))
async def kek(message: types.Message):
    kek1 = await select_user(message.from_user.id)
    print(kek1)
