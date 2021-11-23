from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup

from keyboards.default.birthday_buttons import dbirth_buttons, mbirth_buttons
from loader import dp, bot
from states import Birthday
from utils.db_api import quick_commands

months = {'Январь': 1,
          'Февраль': 2,
          'Март': 3,
          'Апрель': 4,
          'Май': 5,
          'Июнь': 6,
          'Июль': 7,
          'Август': 8,
          'Сентябрь': 9,
          'Октябрь': 10,
          'Ноябрь': 11,
          'Декабрь': 12,
          }


@dp.message_handler(CommandStart(deep_link='reg'))
async def registration(message: types.Message):
    await message.answer('Напиши год рождения (только бот будет знать твой возраст). Например: 1987, 2002 ...', reply_markup=ReplyKeyboardMarkup())
    await Birthday.year.set()

@dp.message_handler(state=Birthday.year)
async def year(message: types.Message, state: FSMContext):
    year_user = message.text
    current_data = datetime.now().year
    if year_user.isdigit() and int(year_user) in range(current_data-80, current_data-8):
        await state.update_data(year=year_user)
        await message.answer("Теперь напиши месяц своего дня рождения", reply_markup=mbirth_buttons)
        await Birthday.month.set()
    else:
        await message.answer("Не обманывай бота, я хочу внести тебя в базу данных! Напиши реальный год рождения)")
        await bot.send_animation(chat_id=message.chat.id, animation='https://c.tenor.com/d3U7GGssSKMAAAAd/steve-rambo-fanclub1.gif')
        await Birthday.year.set()
@dp.message_handler(state=Birthday.month)
async def year(message: types.Message, state: FSMContext):
    if message.text in months:
        month_user = months[message.text]
        await state.update_data(month=month_user)
        await message.answer("И последнее, день рождения", reply_markup=dbirth_buttons)
        await Birthday.day.set()
    else:
        user = message.from_user.full_name
        await message.answer(f"Я вот не могу понять, я тебе выдал кнопки и надо было просто нажать) И помни:")
        await bot.send_animation(chat_id=message.chat.id, animation='https://c.tenor.com/O5qrLn0I698AAAAd/steve-rambo-thats-not-my-problem-its-yours.gif')
        await Birthday.month.set()
@dp.message_handler(state=Birthday.day)
async def year(message: types.Message, state: FSMContext):
    day = message.text
    if day.isdigit() and int(day) in range(1, 32):
        await message.answer("Спасибо, ты в базе данных!", reply_markup=types.ReplyKeyboardRemove())
        states = await state.get_data()
        year = states.get('year')
        month = states.get('month')
        await quick_commands.add_user(id=message.from_user.id,
                            username=message.from_user.username, full_name=message.from_user.full_name, bd_year=int(year), bd_month=int(month), bd_day=int(day))
        await state.finish()
    else:
        user = message.from_user.full_name
        await message.answer(f"Я вот не могу понять, я тебе выдал кнопки и надо было просто нажать) И помни:")
        await bot.send_animation(chat_id=message.chat.id, animation='https://c.tenor.com/O5qrLn0I698AAAAd/steve-rambo-thats-not-my-problem-its-yours.gif')
        await Birthday.day.set()

