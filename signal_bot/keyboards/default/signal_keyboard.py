from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

crypto_name = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BTC"),
            KeyboardButton(text="SOL"),
            KeyboardButton(text="BNB"),
            KeyboardButton(text="XRP")
        ],
        [
            KeyboardButton(text="KSM"),
            KeyboardButton(text="ADA"),
            KeyboardButton(text="DOT"),
            KeyboardButton(text="DOGE")
        ], [
            KeyboardButton(text="NEAR"),
            KeyboardButton(text="TRON"),
            KeyboardButton(text="MOVR"),
            KeyboardButton(text="BNT")
        ],
    ],
    resize_keyboard=True
)

long_short = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Long"),
        KeyboardButton(text='Short')
    ]], resize_keyboard=True)

leverage = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="1"),
        KeyboardButton(text='2-3'),
        KeyboardButton(text='3-5'),
        KeyboardButton(text='5-10'),
        KeyboardButton(text='10-20'),
        KeyboardButton(text='20-50'),
        KeyboardButton(text='50-100')
    ]], resize_keyboard=True)


def math_calc(long_or_short, price, percent):
    a, z = 1 if price > 1 else 4, 1
    kits = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    percent = abs(percent) if long_or_short == 'Long' else percent
    for i in range(4):
        z += percent
        kits.insert(KeyboardButton(text=round(price * z, a)))
    return kits


comment_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='-')]], resize_keyboard=True)


post_or_not_key = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="На оба канала"),
        KeyboardButton(text='На приватный канал'),
        KeyboardButton(text='Не постить')
    ]], resize_keyboard=True)
