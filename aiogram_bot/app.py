from handlers.groups.bd_today import birthday_today
from utils.db_api.db_gino import db
from utils.misc.crypto import crypto_values
from utils.redis.redis_db import redis_update
from utils.set_def_com import set_default_commands
from loader import scheduler
from utils.db_api import db_gino


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    # print("Чистим базу")
    # await db.gino.drop_all()

    print("Создаем таблицы")
    await db.gino.create_all()

    print("Готово")
    await on_startup_notify(dp)
    await set_default_commands(dp)
    crypto_values()
    redis_update()
    birthday_today()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    scheduler.start()

    executor.start_polling(dp, on_startup=on_startup)
