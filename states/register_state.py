from aiogram.dispatcher.filters.state import State, StatesGroup

class Register(StatesGroup):
    full_name = State()
    phone_number = State()
