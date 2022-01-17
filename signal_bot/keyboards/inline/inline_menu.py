import payment
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards import inline

my_list = {'price': '💰Сколько стоит подписка?', 'why': '🤔Почему именно мы?', 'buy': '🛒Приобрести доступ',
           'knowledge': '👨‍🎓Какие знания мне необходимы?'}
menu_cd = CallbackData('show', 'level', 'cat', 'subcat', 'tariff', 'pay')


async def make_callback(level, cat='0', subcat='0', tariff='0', pay='0'):
    return menu_cd.new(level=level, cat=cat, subcat=subcat, tariff=tariff, pay=pay)


async def cat_keyboard():
    lvl = 0
    markup = InlineKeyboardMarkup(row_width=1)
    for items in my_list:
        callback_data = await make_callback(level=lvl + 1, cat=items)
        markup.insert(
            InlineKeyboardButton(text=my_list[items], callback_data=callback_data)
        )
    return markup


async def subcat_keyboard(cat):
    lvl = 1
    my_pop_list = {'price': '💰Сколько стоит подписка?', 'why': '🤔Почему именно мы?', 'buy': '🛒Приобрести доступ',
                   'knowledge': '👨‍🎓Какие знания мне необходимы?'}
    my_pop_list.pop(cat)
    markup = InlineKeyboardMarkup(row_width=1)
    for items in my_pop_list:
        callback_data = await make_callback(level=lvl, cat=items)
        markup.insert(
            InlineKeyboardButton(text=my_pop_list[items], callback_data=callback_data)
        )
    markup.row(InlineKeyboardButton(text='↩️Назад', callback_data=await make_callback(level=0)))

    return markup


async def subscribe_keyboard():
    lvl = 2
    markup = InlineKeyboardMarkup(row_width=1)
    sub_period, x = ("Месяц: 50$", '3 Месяца: 130$', '6 Месяцев: 250$', 'Пожизненно: 450$'), 0
    for sub in sub_period:
        x = x + 1
        callback_data = await make_callback(level=lvl + 1, tariff=x)
        markup.insert(
            InlineKeyboardButton(text=sub, callback_data=callback_data)
        )
    markup.row(InlineKeyboardButton(text='↩️Назад', callback_data=await make_callback(level=0)))
    return markup


async def pay_method_keyboard(tariff):
    lvl = 3
    markup = InlineKeyboardMarkup(row_width=1)
    pay_methods = {'sber': '🇷🇺 Сбербанк', 'mono': '🌍Apple pay/Google pay/🇺🇦LiqPay', 'privat': '🌍Visa/Mastercard',
                   'crypto_wallet': '💵 Crypto wallet'}
    for i in pay_methods:
        callback_data = await make_callback(level=4, tariff=tariff, pay=i)
        markup.insert(
            InlineKeyboardButton(text=pay_methods[i], callback_data=callback_data)
        )
    markup.row(InlineKeyboardButton(text='↩️Назад', callback_data=await make_callback(level=lvl - 1)))
    return markup
