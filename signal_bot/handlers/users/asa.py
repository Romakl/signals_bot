import asyncio

import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from termcolor import colored

from keyboards.default.signal_keyboard import *
from loader import dp, bot
from states.signal import Signal
from utils.misc.calculations import avg
from utils.misc.get_url import get_url

reverse_dict = {'Long': 'Short', "Short": 'Long'}


@dp.message_handler(Command('signal'))
async def signal_set(message: types.Message):
    await message.answer('Какую крипту сегодня будем сегодня постить?', reply_markup=crypto_name)
    await Signal.name.set()


@dp.message_handler(state=Signal.name)
async def year(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text.upper())
    price= await get_url(message.text)
    if price is not None:
        await state.update_data(price=price)
        await message.answer('Long или Short позиция?', reply_markup=long_short)
        await Signal.short_long.set()
    else:
        await message.answer('Нет такой валюты, давай по новой Миша, все х...')
        await Signal.name.set()


@dp.message_handler(state=Signal.short_long)
async def year(message: types.Message, state: FSMContext):
    await state.update_data(position=message.text)
    await message.answer('Какое плече?', reply_markup=leverage)
    await Signal.leverage.set()


@dp.message_handler(state=Signal.leverage)
async def year(message: types.Message, state: FSMContext):
    await state.update_data(leverage=message.text)
    states = await state.get_data()
    await message.answer('Какой вход в позицию?',
                         reply_markup=math_calc(reverse_dict[states.get('position')], states.get('price'), -0.02))
    await Signal.kit.set()


@dp.message_handler(state=Signal.kit)
async def year(message: types.Message, state: FSMContext):
    await state.update_data(kit=message.text)
    states = await state.get_data()
    await message.answer('Каких минимальных целей ждать?',
                         reply_markup=math_calc(states.get('position'), states.get('price'), -0.05))
    await Signal.goals.set()


@dp.message_handler(state=Signal.goals)
async def year(message: types.Message, state: FSMContext):
    await state.update_data(goals=message.text)
    states = await state.get_data()
    await message.answer('Какой стоп ставить?',
                         reply_markup=math_calc(reverse_dict[states.get('position')], states.get('price'), -0.03))
    await Signal.stop.set()


@dp.message_handler(state=Signal.stop)
async def year(message: types.Message, state: FSMContext):
    await state.update_data(stop=message.text)
    await message.answer('Добавить коммент?', reply_markup=comment_keyboard)
    await Signal.comment.set()


@dp.message_handler(state=Signal.comment)
async def comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    states = await state.get_data()
    tags = f'#{states.get("name")} #Спот #Инвестиции' if states.get('leverage') == '1' else \
        f"#{states.get('name')} {states.get('position').lower()} {states.get('leverage')} плече"
    kit = f'{states.get("kit")}'
    goals = avg(str(states.get('goals')), states.get('position'))
    stops = f"{states.get('stop')}"
    comments = ''if states.get('comment') == '-' else f'Коммент: {states.get("comment")}\n\n'
    await message.answer("Постить это???")
    final_result = (f'{tags}\n\n'
                         f'<b>💸С каких позиций брать:</b> {kit}\n\n'
                         f'<b>📈Цели:</b> <tg-spoiler>{goals[0]}</tg-spoiler>\n\n'
                         f'<b>💵Средняя:</b> {goals[1]}\n\n{comments}'
                         f'<b>🚫Стоп:</b> {stops}🚫')
    await message.answer(final_result, reply_markup=post_or_not_key)
    await Signal.check.set()


@dp.message_handler(state=Signal.check)
async def post_or_not(message: types.Message, state: FSMContext):
    states = await state.get_data()
    tags = f'#{states.get("name")} #Спот #Инвестиции' if states.get('leverage') == '1' else \
        f"#{states.get('name')} {states.get('position').lower()} {states.get('leverage')} плече"
    kit = f'{states.get("kit")}'
    goals = avg(str(states.get('goals')), states.get('position'))
    stops = f"{states.get('stop')}"
    comments = ''if states.get('comment') == '-' else f'Коммент: {states.get("comment")}\n\n'
    final_result = (f'{tags}\n\n'
                         f'<b>💸С каких позиций брать:</b> {kit}\n\n'
                         f'<b>📈Цели:</b> <tg-spoiler>{goals[0]}</tg-spoiler>\n\n'
                         f'<b>💵Средняя:</b> {goals[1]}\n\n{comments}'
                         f'<b>🚫Стоп:</b> {stops}🚫')
    if message.text == 'На оба канала':
        await state.finish()
        await bot.send_message(chat_id=-1001128738537, text=final_result)
    elif message.text == 'На приватный канал':
        await state.finish()
        await message.answer('Пост направлен на приватный канал', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(chat_id=-1001128738537, text=final_result)
    else:
        await state.finish()
        await message.answer('Это постить мы не будем 🤗🤗🤗', reply_markup=types.ReplyKeyboardRemove())
