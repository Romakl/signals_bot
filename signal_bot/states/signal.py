from aiogram.dispatcher.filters.state import StatesGroup, State


class Signal(StatesGroup):
    name = State()
    short_long = State()
    leverage = State()
    kit = State()
    goals = State()
    stop = State()
    check = State()
    comment = State()