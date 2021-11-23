from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import seminar, prepare, buybot

akadembutton = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Семинар",
                                                callback_data=seminar.new(item_name='seminar')
                                            ),

                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="ПопкоОметр",
                                                callback_data=seminar.new(item_name='Popko')
                                            ),
                                            InlineKeyboardButton(
                                                text="День Рождения",
                                                callback_data=seminar.new(item_name='Birthday')
                                            ),

                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Социальный рейтинг",
                                                callback_data=seminar.new(item_name='boyz')
                                            ),
                                            InlineKeyboardButton(
                                                text="Поделись разработкой с другом",
                                                switch_inline_query="BuyBot"
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Скрыть клавиатуру",
                                                callback_data=seminar.new(item_name='close')
                                            )
                                        ],
                                    ])

prepare_sem = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text="Цивільне",
                                               callback_data=prepare.new(discipline_name='civil')
                                           ),
                                           InlineKeyboardButton(
                                               text="Адміністративне",
                                               callback_data=prepare.new(discipline_name='administrative')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text="Муніципальне",
                                               callback_data=prepare.new(discipline_name='municipal')
                                           ),
                                           InlineKeyboardButton(
                                               text="Трудове",
                                               callback_data=prepare.new(discipline_name='labor')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text="Судове",
                                               callback_data=prepare.new(discipline_name='court')
                                           ),
                                           InlineKeyboardButton(
                                               text="ТМПР/Логіка",
                                               callback_data=prepare.new(discipline_name='logic')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text="Вернуться назад",
                                               callback_data=prepare.new(discipline_name='back_to_list')
                                           ),

                                       ],
                                   ])
seminar_timer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Еще раз",
                callback_data=seminar.new(item_name='seminar')
            ),

        ],
        [
            InlineKeyboardButton(
                text="Вернуться назад",
                callback_data=prepare.new(discipline_name='back_to_list')
            ),

        ],
    ])

reg_keyboard = InlineKeyboardMarkup()
reg_link = InlineKeyboardButton(text='Зарегистрироваться', url='https://t.me/JacqueFrescoTimerBot?start=reg')
reg_keyboard.insert(reg_link)

share_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🤖Почему именно мой бот?🤖",
                callback_data=buybot.new(name="why")
            ),

        ],
        [
            InlineKeyboardButton(
                text="💵Цена бота💵",
                callback_data=buybot.new(name="price")
            ),

        ],
    ])

buy_keyboard = InlineKeyboardMarkup()
buy_link = InlineKeyboardButton(text='Узнать поподробнее', url='https://t.me/razgildiai_dev_bot?start=buy')
buy_keyboard.insert(buy_link)
