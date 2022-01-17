from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(id: int, username: str, full_name: str, liquidation_day: int):
    try:
        user = User(id=id, username=username, full_name=full_name, liquidation_day=liquidation_day)
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


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total
