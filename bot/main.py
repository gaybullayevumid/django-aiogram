import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from buttons import button
from api import create_user, create_feedback
from states import FeedbackState
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram import Router

API_TOKEN = '6881014528:AAHxuHUw-eQoheEIVgRcA7G9o0IJlJaXWrY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Initialize storage
dp = Dispatcher(storage=storage)

# Create a router object for message handlers
router = Router()

# Handler for /start and /help commands
@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends `/start` or `/help` command.
    """
    await message.reply("Assalomu alaykum!\nDjango-aiogram botimizga xush kelibsiz!", reply_markup=button)
    create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)

# Handler for feedback initiation
@router.message(lambda msg: msg.text and msg.text.startswith("Talab va Takliflar"))
async def feedback_1(message: types.Message):
    await message.answer("Xabar matnini yuboring.")
    # Set the state using FSMContext
    fsm_context = FSMContext(storage=message.bot.get('storage'), key=message.from_user.id)
    await fsm_context.set_state(FeedbackState.body)

# Handler for feedback submission (when in FeedbackState.body)
@router.message()
async def feedback_2(message: types.Message):
    # Check the state using FSMContext
    fsm_context = FSMContext(storage=message.bot.get('storage'), key=message.from_user.id)
    state = await fsm_context.get_state()
    
    if state == FeedbackState.body:
        await message.answer(create_feedback(message.from_user.id, message.text))
        await fsm_context.clear()  # Clear the state after completion
    else:
        await message.answer(message.text)

# Main function to start polling
async def main():
    # Register the router with the dispatcher
    dp.include_router(router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
