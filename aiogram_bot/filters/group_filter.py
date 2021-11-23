from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import group_id
from utils.db_api.quick_commands import select_user


class IsGroup(BoundFilter):
    async def check(self, call: types.CallbackQuery) -> bool:
        return call.message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPER_GROUP
        )


class ChatIdFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.id in (
            group_id,
            await select_user(message.from_user.id))
