import os

from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Item


Tariff_1 = Item(
    title="Тариф №1",
    description='Покупая тариф №1 - Вы получаете доступ к закрытому клубу на 1 месяц. Обратите внимание на то, '
                'что этот тариф тестовый и цена выставлена в 1$ и провайдер тестовый, по этому если вы даже оплатите '
                'тариф, то деньги не будут списаны с вас)',
    currency="USD",
    prices=[
        LabeledPrice(
            label="Тариф №1",
            amount=1_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-0
        ),
    ],
    start_parameter="create_invoice_tesla_model_s",
    photo_url="https://i.redd.it/fhihrikio7y71.jpg",
)

Tariff_2 = Item(
    title="Тариф №2",
    description="Покупая тариф №2 - Вы получаете доступ к закрытому клубу на 3 месяца",
    currency="USD",
    prices=[
        LabeledPrice(
            label="Тариф ",
            amount=150_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-20_00
        ),
    ],
    start_parameter="create_invoice_tesla_model_s",
    photo_url='https://i.redd.it/fhihrikio7y71.jpg'
)
Tariff_3 = Item(
    title="Тариф №3",
    description="Покупая тариф №3 - Вы получаете доступ к закрытому клубу на 6 месяцев",
    currency="USD",
    prices=[
        LabeledPrice(
            label="Тариф ",
            amount=300_00
        ),
        LabeledPrice(
            label="Скидка",
            amount=-50_00
        ),
    ],
    start_parameter="create_invoice_tesla_model_s",
    photo_url="https://i.pinimg.com/originals/47/8f/7c/478f7c794f244f2ca939753dd305b05d.jpg",
)

Tariff_4 = Item(
    title="Тариф №4",
    description="Покупая тариф №4 - Вы получаете доступ к закрытому клубу на всегда",
    currency="USD",
    prices=[
        LabeledPrice(
            label="Тариф ",
            amount=450_00
        ),
    ],
    start_parameter="create_invoice_tesla_model_s",
    photo_url="https://www.memesmonkey.com/images/memesmonkey/6c/6c6910f475e85b05361d4603600f69e0.jpeg",
)

