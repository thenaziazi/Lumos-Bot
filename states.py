
from aiogram.fsm.state import StatesGroup, State


class Questionnarie(StatesGroup):
    full_name = State()
    age = State()
    gender = State()
    profession = State()
