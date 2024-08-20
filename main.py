import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from config import Token
from db import Database

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = Bot(token=Token,parse_mode=ParseMode.HTML)

dp = Dispatcher()
db = Database("database.db")

Super_admin = 6543698942

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if db.check_user(user_id=message.from_user.id):
        await message.answer(f"<b>Assalomu Aleykum.Xurmatli {message.from_user.mention_html()}\nSiz bazamizda allaqachon borsiz.Reklamarni kuting.</b>")

    else:
        await message.answer(f"<b>Assalomu Aleykum. Xurmatli {message.from_user.mention_html()}\nEndi reklamalar sizga ham yuboriladi.</b>")
        db.add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
        print("Databasega saqlandi !")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
