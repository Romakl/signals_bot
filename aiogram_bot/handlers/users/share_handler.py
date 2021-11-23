from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buybot
from loader import dp

@dp.message_handler(buybot.filter(name="why"))
async def price(call: CallbackQuery):
    call.message.answer('lol')


@dp.message_handler(buybot.filter(name="price"))
async def price(call: CallbackQuery):
    call.message.answer('lol')
