import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from config import Token
from db import Database
from keyboards import advertising
from aiogram.fsm.context import FSMContext
from States import Advertisement

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = Bot(token=Token,parse_mode=ParseMode.HTML)

dp = Dispatcher()
db = Database("database.db")

Super_admin = "Super Admin ID (Integer)"

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state:FSMContext):
    if message.from_user.id == Super_admin:
        await message.answer("<b>Assalomu Aleykum Admin.Xush kelibsiz.</b>",reply_markup=advertising)

        @dp.message(F.text == "reklama yuborish")
        async def advertising_(message:types.message,state:FSMContext):
            await state.set_state(Advertisement.text)
            await message.answer("<b>Reklamaning textini yuboring:</b>")

            @dp.message(Advertisement.text)
            async def advertising_(message:types.Message,state:FSMContext):
                await state.update_data(text=message.text)
                await state.set_state(Advertisement.photo)
                await message.answer("<b>Reklamaning rasmini yuboring:</b>")

            @dp.message(Advertisement.photo)
            async def advertising_(message:types.Message,state:FSMContext):
                await state.update_data(image=message.photo[-1].file_id)
                await state.set_state(Advertisement.finish)
                data = await state.get_data()
                text = data.get("text","Unknown")
                image =  data.get("image","Unknown")

                for user in db.get_ids_users:
                    await bot.send_photo(chat_id=user[0],photo=image,caption=text)


    elif db.check_user(user_id=message.from_user.id):
        await message.answer(f"<b>Assalomu Aleykum.Xurmatli {message.from_user.mention_html()}\nSiz bazamizda allaqachon borsiz.Reklamarni kuting.</b>")

    else:
        await message.answer(f"<b>Assalomu Aleykum. Xurmatli {message.from_user.mention_html()}\nEndi reklamalar sizga ham yuboriladi.</b>")
        db.add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
        print("Databasega saqlandi !")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
