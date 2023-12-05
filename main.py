# Я буду писать всё чтобы нахуй трезвым не ахуеть после пъянки

# Импорт модулей
import logging
import sqlite3
import sys

from aiogram import F, Bot, Dispatcher, types
from config import BOT_TOKEN, GROUP_ID
from aiogram.fsm.context import FSMContext

from aiogram.types import (
    Message,
    URLInputFile
)
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command


con = sqlite3.connect("defaulters.db")
cur = con.cursor()


storage = MemoryStorage()
bot = Bot(BOT_TOKEN, parse_mode="html")
dp = Dispatcher(storage=storage)
try:
    if sys.argv[1] == "--fuckery":
    # Дебаг хуйня TODO: включение на аргумент
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] {%(filename)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
        )

        @dp.message(Command("id"))
        async def get_id(message: Message, state: FSMContext):
            await message.answer(str(message.chat.id))
    else:
        pass
except Exception:
    pass

@dp.message()
async def base_shit(message: types.Message):
    # Проверяем, является ли пользователь участником группы
    match message.chat.id:
        case GROUP_ID:
            try:
                match message.text.lower():
                    case "иди нахуй":
                        await message.reply("Сам иди бля, быдло")
                    case _:
                        pass
            except Exception:
                pass # Бля, денис, я явно набухался, будь так добр, распиши некоторые команды боту





if __name__ == "__main__":

    dp.run_polling(bot)
