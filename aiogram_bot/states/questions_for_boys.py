from aiogram.dispatcher.filters.state import StatesGroup, State


class Birthday(StatesGroup):
    year = State()
    month = State()
    day = State()
    finish = State()


class SeminarAsk(StatesGroup):
    how_many_questions = State()
    who_absent = State()
