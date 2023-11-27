# Я буду писать всё чтобы нахуй трезвым не ахуеть после пъянки

# Импорт модулей
import logging
import sqlite3

from aiogram import F, Bot, Dispatcher, types
from config import BOT_TOKEN
from aiogram.fsm.context import FSMContext

from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

# Дебаг хуйня TODO: включение на аргумент
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(filename)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

con = sqlite3.connect("defaulters.db")
cur = con.cursor()


storage = MemoryStorage()
bot = Bot(BOT_TOKEN, parse_mode="html")
dp = Dispatcher(storage=storage)


@dp.message(Command("id"))
async def get_id(message: Message, state: FSMContext):
    await message.answer(str(message.from_user.id))


if __name__ == "__main__":
    dp.run_polling(bot)
