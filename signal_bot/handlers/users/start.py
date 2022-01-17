from nis import cat
from typing import Union

import payment as payment
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import CallbackQuery, ContentTypes, ContentType

from data.config import PROVIDER_TOKEN
from data.items import Tariff_3, Tariff_1, Tariff_2, Tariff_4
from keyboards.inline.inline_menu import *
from loader import dp, bot
from aiogram.utils.markdown import hlink

from utils.db_api.quick_commands import add_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await list_cat(message)


async def list_cat(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await cat_keyboard()
    caption = 'Воспользуйся кнопками ниже, чтобы узнать об этом канале поподробнее\n\n' \
              'А также можешь подписаться на наши каналы, где мы часто постим полезную информацию:\n' \
              f"{hlink('Основной канал', 'https://t.me/RichWhale_official')}\n" \
              f"{hlink('Twitter', 'https://twitter.com/Mr_RichWhale')}\n" \
              f"{hlink('TikTok', 'https://vm.tiktok.com/ZML1Jr82F/')}\n"
    if isinstance(message, types.Message):
        await message.answer(f'Привет, {message.from_user.full_name}!')
        await message.answer_photo(photo='https://memepedia.ru/wp-content/uploads/2019/06/stonks-template-768x576.png',
                                   caption=caption, reply_markup=markup)
        # link = await bot.create_chat_invite_link(chat_id=-1001128738537, member_limit=1)
        # await message.answer(f"Привет, {message.from_user.full_name}!\n\nДобро пожаловать на наш закрытый канал:\n\n"
        #                      f"{link.invite_link}")
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_caption(caption)
        await call.message.edit_reply_markup(markup)


async def list_subcat(call: CallbackQuery, cat, **kwargs):
    markup = await subcat_keyboard(cat)
    if cat == 'price':
        await call.message.edit_caption(
            'Стоимость подписки на закрытый клуб составляет символические:\n\n50$ - 1 месяц\n130$ - 3 месяца\n250$ - '
            '6 месяцев\n450$- пожизненно')
        await call.message.edit_reply_markup(reply_markup=markup)
    if cat == 'why':
        await call.message.edit_caption("У нас есть канал с отзывами про <b>{}</b>. Лично от себя добавлю (Я "
                                        "программист, "
                                        "который пишет этот текст) скажу что клуб реально хороший(Мне за эти слова не "
                                        "платили). Конечно же Кэп не гуру и не все сделки будут успешными, но он точно "
                                        "профи в своей сфере, по моей статистике <b>где то 70-80% сделок дают "
                                        "результат</b> и "
                                        "грамотные стопы от Кэпа спасают даже самую плохую ситуацию. Так же я лично "
                                        "подметил очень ламповое комьюнити, которое помогает новичкам, даёт советы по "
                                        "разным валютам и постит мемы)".format(
            hlink("Клуб", 'https://t.me/Otzivy_RichWhale')))
        await call.message.edit_reply_markup(reply_markup=markup)
    if cat == 'buy':
        await choose_sub(call)

    if cat == 'knowledge':
        link_dict = {"Что такое Binance?": "https://youtu.be/5ni649349L4",
                     "Что такое P2P транзакции?": "https://youtu.be/jl87i65MD9I",
                     "Что такое стоп-лимит ордер?": "https://youtu.be/BJIZI-8KtBM",
                     "Что такое ОСО ордер?": "https://youtu.be/VzxgT4LXm28",
                     "Логика движения рынка?": "https://youtu.be/CE2QfmaJCiw",
                     "Самые популярные паттерны": "https://youtu.be/BDIBo4HBbMQ",
                     "Что такое маржинальная торговля?": "https://youtu.be/AC6koBc9rcg",
                     "Что такое фьючерсная торговля?": "https://youtu.be/lwHArSK9KCY"}
        kek = '\n'.join([hlink(i, link_dict[i]) for i in link_dict])
        await call.message.edit_caption('У нас довольно низкий порог входа и в этом канале есть как новички так и '
                                        'профи с большим стажем работы. Но хорошим тоном будет посмотреть базовые '
                                        f'основы трейдинга от наших коллег:\n{kek}')
        await call.message.edit_reply_markup(reply_markup=markup)


async def choose_sub(call: CallbackQuery, **kwargs):
    await call.message.edit_caption('У нас есть такие тарифы:')
    await call.message.edit_reply_markup(reply_markup=await subscribe_keyboard())


async def pay_method(call: CallbackQuery, tariff, **kwargs):
    await call.message.edit_caption('Мы принимаем оплату на:')
    await call.message.edit_reply_markup(reply_markup=await pay_method_keyboard(tariff))


async def final_result(call: CallbackQuery, tariff, pay, **kwargs):
    if pay == 'crypto_wallet':
        await call.message.answer('На данный момент мы не автоматизировали систему с крипто-кошельком, по этому нужно '
                                  'сделать все вручную 😭.\n\nДля оплаты нужно отправить выбранную вами сумму в USDT и '
                                  'отправить на крипто-адрес котрый будет написан ниже, после чего напишите '
                                  '@Your_Kapitan об оплате и он отправит вам пригласительную ссылку, если вы не '
                                  'знаете как отправить на кошелек деньги видео инструкция ниже:')
        await call.message.answer('TBPXo9LEW4vbtAsyyMENDHvihcvfmNnBKo')
        await bot.send_video(call.from_user.id, video=open('photos/telegram-cloud-document-2-5411617531209192699.mp4',
                                                           'rb'), caption='Учитывайте комиссию в 1$')
    tariff_dict = {'1': Tariff_1.generate_invoice(), '2': Tariff_2.generate_invoice(),
                   '3': Tariff_3.generate_invoice(), '4': Tariff_4.generate_invoice()}
    pay_dict = {'sber': PROVIDER_TOKEN, 'mono': PROVIDER_TOKEN, 'privat': PROVIDER_TOKEN}
    await bot.send_invoice(chat_id=call.from_user.id, **tariff_dict[tariff],
                           provider_token=pay_dict[pay], payload="first_tariff")


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    print('order_info')
    print(pre_checkout_query.order_info)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    await message.answer('Ура! Платеж на сумму `{total_amount} {currency}` совершен успешно!'.format(total_amount=message.successful_payment.total_amount // 100,
                                                             currency=message.successful_payment.currency))
    order_tariff = message.successful_payment.total_amount
    tariff_dict =  {50: 30, 130: 61, 250: 183, 450: None}
    id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    import datetime
    tod = datetime.datetime.now()
    d = lambda x: datetime.timedelta(days=x)
    liquidation_day = tod + d(tariff_dict[order_tariff])
    print(message.successful_payment.order_info)
    await add_user(id=id, username=username, full_name=full_name, liquidation_day=liquidation_day)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    level = callback_data.get('level')
    cat = callback_data.get('cat')
    subcat = callback_data.get('subcat')
    tariff = callback_data.get('tariff')
    pay = callback_data.get('pay')
    levels = {
        '0': list_cat,
        '1': list_subcat,
        '2': choose_sub,
        '3': pay_method,
        '4': final_result

    }
    current_level = levels[level]

    await current_level(call, cat=cat, subcat=subcat, tariff=tariff, pay=pay)
