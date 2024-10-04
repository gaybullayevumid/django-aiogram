from aiogram.fsm.state import State, StatesGroup

class FeedbackState(StatesGroup):
    body = State()