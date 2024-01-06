import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from config import Token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Token)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Bot eshityapti!")
    print(message.from_user.id)
    await bot.send_photo(chat_id=6716993468, photo="https://flstrefa.pl/images/zdjecie/promocja.jpg", caption="Reklama olamiz ✅")



print(f"Message send to 6716993468")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
