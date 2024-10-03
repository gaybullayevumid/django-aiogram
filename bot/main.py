import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

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
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# Echo handler
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
