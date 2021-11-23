from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user.full_name
    await message.answer(f'{user}, привет! Это Жак Фреско 2.0!\n'
                         '\n'
                         'Это новая верисия бота на 3000+ строк кода. Бот использует многие функции и библиотеки от '
                         'Postgresql до Docker и Django\n '
                         '\n'
                         'Так же бот стал асинхронным, что значительно ускорит работу. По команде /list можно увидеть '
                         'клавиатуру группы\n '
                         '\n'
                         'Так же Рома полноценно стал Middle PyDev и вышел на фриланс!(Именно по этому я выгляжу '
                         'убитым на парах, лол)\n '
                         '\n'
                         'Так же бот теперь официально работает 24/7 на Amazon server. Если не хватает функционала, '
                         'пиши и Рома добавит\n')