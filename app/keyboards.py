from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Профиль'),
    KeyboardButton(text='Ключи')]
],
                        resize_keyboard=True,
                        input_field_placeholder='Выберите пункт меню.')