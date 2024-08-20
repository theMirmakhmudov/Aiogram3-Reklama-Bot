from aiogram.fsm.state import StatesGroup,State

class Advertisement(StatesGroup):
    text = State()
    photo =  State()
    finish = State()