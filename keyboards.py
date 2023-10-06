from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


# Створення кнопок
main_kb = [
    [KeyboardButton(text='Інформація'),
     KeyboardButton(text='Товари')],
    [KeyboardButton(text='Контакти')]
]

# Створення клавіатури
main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Оберіть пункт нижче')


# Створення контактів
socials = InlineKeyboardMarkup(inline_keyboard=[
    # Будь яке ваше посилання
    [InlineKeyboardButton(
        text='Telgram', url='https://www.google.com.ua/')],
    [InlineKeyboardButton(
        text='YouTube', url='https://www.google.com.ua/')]
])


# Створення каталогу товарів
catalog = InlineKeyboardMarkup(inline_keyboard=[
    # Товари також для приклау і можуть бути замінені
    [InlineKeyboardButton(text='Bitcoin', callback_data='Bitcoin')],
    [InlineKeyboardButton(text='Ethereum', callback_data='Ethereum')],
    [InlineKeyboardButton(text='Dogecoin', callback_data='Dogecoin')]
])


# Інформація про бота
inform = InlineKeyboardMarkup(inline_keyboard=[
    # Будь яка інформація про бота
    [InlineKeyboardButton(
        text='Наш сайт', url='https://uk.wikipedia.org/wiki/')]
])
