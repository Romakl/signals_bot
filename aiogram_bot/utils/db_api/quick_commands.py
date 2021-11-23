from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(id: int, username: str, full_name: str, bd_year: int, bd_month: int, bd_day: int):
    try:
        user = User(id=id, username=username, full_name=full_name, bd_year=bd_year, bd_month=bd_month, bd_day=bd_day)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    try:
        user = await User.query.where(User.id == id).gino.first()
        return user.id
    except:
        pass


async def users_bd_m(bd_month: int):
    user = await User.select('full_name', 'bd_day').where(User.bd_month == bd_month).gino.all()
    return user


async def users_bd_d(bd_day, bd_month):
    user = await User.select('full_name', 'username').where(bd_month == User.bd_month).where(
        bd_day == User.bd_day).gino.all()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_email(id, email):
    user = await User.get(id)
    await user.update(email=email).apply()
