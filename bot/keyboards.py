from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)

keyboard_1 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
button_1 = KeyboardButton(text='/holidays_ru')
button_2 = KeyboardButton(text='/holidays_en')
keyboard_1.add(button_1, button_2)