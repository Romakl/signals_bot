from datetime import datetime

from aiogram.types import CallbackQuery

from data.config import group_id
from keyboards.inline.callback_datas import seminar
from keyboards.inline.choice_buttons import reg_keyboard
from loader import dp, scheduler, bot
from utils.db_api import quick_commands


@dp.callback_query_handler(seminar.filter(item_name='Birthday'))
async def bd_check(call: CallbackQuery):
    check_registration = await quick_commands.select_user(id=call.from_user.id)
    users_check = await quick_commands.users_bd_m(bd_month=datetime.now().month)
    if bool(check_registration):
        bd_this_month = 'В этом месяце:\n' + ''.join(
            [f'{i.bd_day} числа у {i.full_name} день рождения\n' for i in users_check])
        no_bd = 'В этом месяце нет дней рождений'
        await call.message.answer(bd_this_month) if bool(users_check) else await call.message.answer(no_bd)
    else:
        await call.message.answer("Тебя нет в базе данных, пройди короткую регистрацию по кнопке ниже:",
                                  reply_markup=reg_keyboard)


async def bd_today():
    users_bd_today = await quick_commands.users_bd_d(bd_day=datetime.now().day, bd_month=datetime.now().month)
    if bool(users_bd_today):
        if len(users_bd_today) > 1:
            await bot.send_message(chat_id=group_id, text="Сегодня день рождения у {0}. Поздравляю вас от всей души! "
                                                          "Желаю чтобы у вас было всё прекрасно! Чтобы вас окружали "
                                                          "только самые верные друзья. Здоровья, "
                                                          "удачи и любви!".format(
                ' и '.join(i.full_name for i in users_bd_today)))
        else:
            await bot.send_message(chat_id=group_id, text="Сегодня день рождения у {0}. Поздравляю тебя от всей души! "
                                                          "Желаю чтобы у тебя было всё прекрасно! Чтобы тебя окружали "
                                                          "только самые верные друзья. Здоровья, "
                                                          "удачи и любви!".format(
                ''.join(i.full_name for i in users_bd_today)))

    else:
        pass


def birthday_today():
    scheduler.add_job(bd_today, 'cron', hour='8', minute='0')
