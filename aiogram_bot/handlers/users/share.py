from aiogram import types

from keyboards.inline.choice_buttons import buy_keyboard
from loader import dp

@dp.inline_handler(text="BuyBot")
async def buy_bot(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="BuyBot",
                title="Поделись разработкой бота!",
                description="За каждого проданного бота через друзей, даю 20% от прибыли!",
                thumb_url="https://image.freepik.com/free-vector/robot-icon-bot-sign-design-chatbot-symbol-concept-voice-support-service-bot-online-support-bot-vector-stock-illustration_100456-34.jpg",
                input_message_content=types.InputTextMessageContent(
                    message_text="Привет, меня зовут Роман и я разрабатываю чат боты любой сложности. Telegram, "
                                 "Instagram. (возможны другие платформы и мессенджеры Предлагаю :\n1) Разработка под "
                                 "ключ Чат-Бота. Полностью готовый к работе и уникальный в своем классе продукт по ТЗ "
                                 "заказчика.\n2) Подключение Бота к вашему бизнесу.\n3) Подключение Бота к любым "
                                 "инструментам Windows (exel, word, txt и т.д), Google под нужды заказчика.\nИмею "
                                 "несколько заготовок разных типов ботов для более быстрого создания такого, "
                                 "который нужен именно вам. Буду рад взяться за ваш проект и создать бота практически "
                                 "любой сложности в кратчайшие сроки и по доступной цене пиши в ЛС @romainkl! "

                )
            )
        ]
    )
