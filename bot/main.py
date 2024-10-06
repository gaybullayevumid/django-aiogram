# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# import asyncio
# from buttons import button
# from api import create_user, create_feedback
# from states import FeedbackState
# from aiogram.filters import Text
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.fsm.context import FSMContext



# API_TOKEN = '6881014528:AAHxuHUw-eQoheEIVgRcA7G9o0IJlJaXWrY'

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage)

# # Handler for /start and /help commands
# @dp.message(Command(commands=['start', 'help']))
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when the user sends `/start` or `/help` command.
#     """
#     await message.reply("Assalomu alaykum!\nDjango-aiogram botimizga xush kelibsiz!", reply_markup=button)
#     create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)

# @dp.message_handler(Text(startwith="Talab va Takliflar"))
# async def feedback_1(message:types.Message):
#     await message.answer("Xabar matnini yuboring.")
#     await FeedbackState.body.set()

# @dp.message_handler(state=FeedbackState.body)
# async def feedback_2(message: types.Message, state:FSMContext):
#     await message.answer(create_feedback(message.from_user.id, message.text))
#     await state.finish()

# # Echo handler
# @dp.message()
# async def echo(message: types.Message):
#     await message.answer(message.text)

# async def main():
#     # Start polling
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())



import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text  # Correct import
import asyncio
from buttons import button
from api import create_user, create_feedback
from states import FeedbackState
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext


API_TOKEN = '6881014528:AAHxuHUw-eQoheEIVgRcA7G9o0IJlJaXWrY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Initialize storage
dp = Dispatcher(storage=storage)

# Handler for /start and /help commands
@dp.message_handler(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends `/start` or `/help` command.
    """
    await message.reply("Assalomu alaykum!\nDjango-aiogram botimizga xush kelibsiz!", reply_markup=button)
    create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)

# Handler for feedback initiation
@dp.message_handler(Text(startswith="Talab va Takliflar"))  # Correct usage of Text filter
async def feedback_1(message: types.Message):
    await message.answer("Xabar matnini yuboring.")
    await message.state.set_state(FeedbackState.body)

# Handler for feedback submission (when in FeedbackState.body)
@dp.message_handler(state=FeedbackState.body)
async def feedback_2(message: types.Message, state: FSMContext):
    await message.answer(create_feedback(message.from_user.id, message.text))
    await state.clear()  # Clear the state after completion

# Echo handler for all other messages
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Main function to start polling
async def main():
    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
