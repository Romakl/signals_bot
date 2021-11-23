from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import prepare
from keyboards.inline.choice_buttons import akadembutton
from loader import dp


@dp.callback_query_handler(prepare.filter(discipline_name='civil'))
async def civil_law(call: CallbackQuery):
    # await call.message.answer('Сколько вопросов?:')
    # await Seminar_ask.who_apsent.set()
    await call.message.answer(text='https://docs.google.com/document/d/1IAIm-Wud76kgvc9hMZyoxI3Yl22xeXSXEJ0D-8J23Kw'
                                   '/edit?usp=sharing')


@dp.callback_query_handler(prepare.filter(discipline_name='administrative'))
async def administrative_law(call: CallbackQuery):
    await call.message.answer(text="https://docs.google.com/document/d/1LfKseHpH0LliD-kmRb1hD4ejFFlGowD0_GM8PTENqx0"
                                   "/edit?usp=sharing")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(prepare.filter(discipline_name='municipal'))
async def municipal_law(call: CallbackQuery):
    await call.message.answer(text="https://docs.google.com/document/d/1n2Ae2HxesztXpJHP-_yck2IzpFxGMb4lqlT_54JYVgo"
                                   "/edit?usp=sharing")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(prepare.filter(discipline_name='labor'))
async def labor_law(call: CallbackQuery):
    await call.message.answer(
        text="https://docs.google.com/document/d/1yQaDf56J_qNJXg4gp3zU5VUifIi_JAkOpD09Qy4LOc8/edit?usp=sharing")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(prepare.filter(discipline_name='court'))
async def court_law(call: CallbackQuery):
    await call.message.answer(
        text="https://docs.google.com/document/d/1hT73ZdK0trQiMmTAg-jRsLv888RTRnHpp_ANz08F_FM/edit?usp=sharing")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(prepare.filter(discipline_name='logic'))
async def logic_law(call: CallbackQuery):
    await call.message.answer(
        text="https://docs.google.com/document/d/1pFox4hPNfLX4qvBd8DaZDXT-l9Gx4myPa_Wx4TR4Nzw/edit?usp=sharing")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(prepare.filter(discipline_name='back_to_list'))
async def back_to_list(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=akadembutton)
