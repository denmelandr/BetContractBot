import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Проверь наличие файла .env")

bot = Bot(TOKEN)
dp = Dispatcher()

def get_profile_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    
    builder.add(KeyboardButton(
        text="Поспорить", 
        web_app=WebAppInfo(url="https://google.com")
    ))
    
    return builder.as_markup(resize_keyboard=True)

async def start_handler(message: types.Message):

    keyboard = get_profile_keyboard()

    # Создаем клавиатуру
    await message.answer(
        "Привет! Я бот для споров с друзьями через смарт контракты!",
        reply_markup=keyboard
    )

dp.message.register(start_handler, CommandStart())
asyncio.run(dp.start_polling(bot))