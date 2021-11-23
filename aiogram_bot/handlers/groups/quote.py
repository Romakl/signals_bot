from io import BytesIO

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot


@dp.message_handler(Command("q"))
async def create_quote_sticker(message: types.Message):
    chat_id=message.chat.id
    kek = await bot.get_user_profile_photos(user_id=message.from_user.id, limit=0)
    kek=kek.photos[0]
    kek= kek[0].get_file()
    kek = await kek
    print(kek)
    await bot.send_document(chat_id=chat_id, document=kek)
    # await bot.send_photo(chat_id=chat_id, photo=kek)
    # print(kek)
