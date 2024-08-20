from aiogram import types

keyboard_admin_advertisement = [
    [types.KeyboardButton(text="reklama yuborish")]
]

advertising = types.ReplyKeyboardMarkup(keyboard=keyboard_admin_advertisement,resize_keyboard=True,input_field_placeholder="Reklama yuborish uchun bosing")