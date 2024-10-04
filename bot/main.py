import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from buttons import button
from api import create_user, create_feedback

API_TOKEN = '6881014528:AAHxuHUw-eQoheEIVgRcA7G9o0IJlJaXWrY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Handler for /start and /help commands
@dp.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    """
    This handler will be called when the user sends `/start` or `/help` command.
    """
    await message.reply("Assalomu alaykum!\nDjango-aiogram botimizga xush kelibsiz!", reply_markup=button)
    create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)

# Echo handler
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
