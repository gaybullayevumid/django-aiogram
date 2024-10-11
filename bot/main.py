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

API_TOKEN = '6881014528:AAHxuHUw-eQoheEIVgRcA7G9o0IJlJaXWrY'  # Bot tokeni


# Log yozuvlarini sozlash
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher'ni ishga tushirish
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Xotira saqlash tizimini ishga tushirish
dp = Dispatcher(storage=storage)

# Router obyektini yaratish (xabarlarni boshqarish uchun)
router = Router()


# /start va /help komandalarini qabul qiluvchi handler
@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    """
    Ushbu handler foydalanuvchi /start yoki /help komandalarini yuborganida ishlaydi.
    """
    await message.reply("Assalomu alaykum!\nIT Park Feedback botimizga xush kelibsiz!", reply_markup=button)
    create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)


# Foydalanuvchining talab va takliflarini qabul qilishni boshlash
@router.message(lambda msg: msg.text and msg.text.startswith("Talab va Takliflar"))
async def feedback_1(message: types.Message, state: FSMContext):
    await message.answer("Xabar matnini yuboring.")
    # Foydalanuvchining holatini o'rnatish
    await state.set_state(FeedbackState.body)


# Foydalanuvchining xabarini qabul qilish va uni saqlash (FeedbackState.body holatida)
@router.message()
async def feedback_2(message: types.Message, state: FSMContext):
    # Foydalanuvchining joriy holatini tekshirish
    current_state = await state.get_state()

    if current_state == FeedbackState.body:
        await message.answer(create_feedback(message.from_user.id, message.text))
        await state.clear()  # Holatni tozalash
    else:
        await message.answer(message.text)


# Botni ishga tushirish uchun asosiy funksiya
async def main():
    # Routerni dispatcher bilan ro‘yxatdan o‘tkazish
    dp.include_router(router)

    # Pollingni boshlash
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
