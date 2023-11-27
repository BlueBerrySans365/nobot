import logging
from aiogram import F, Bot, Dispatcher, types
from config import BOT_TOKEN
from aiogram.fsm.context import FSMContext

from aiogram.types import (
    Message
)
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(filename)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

storage = MemoryStorage()
bot = Bot(BOT_TOKEN, parse_mode="html")
dp = Dispatcher(storage=storage)

@dp.message(Command("id"))
async def get_id(message: Message, state: FSMContext):
    await message.answer(str(message.from_user.id))


if __name__ == "__main__":
    dp.run_polling(bot)