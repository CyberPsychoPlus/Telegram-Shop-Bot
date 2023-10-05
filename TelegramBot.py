import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery

# Імпорт власної бібліотеки
import keyboards as kb

bot = Bot(token='6226072857:AAHuGs192tdGtFLfFes0odt9lB0qpld1zWc')
dp = Dispatcher()


# Початок праці з ботом
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    # Будь який інший напис замість(Вітаємо!)
    await message.answer('Вітаємо!', reply_markup=kb.main)


# Обробник контактів
@dp.message(F.text == 'Контакти')
async def contacts(message: Message):
    await message.answer('Наші контакти: ', reply_markup=kb.socials)


# Обробник товарів
@dp.message(F.text == 'Товари')
async def catalog(message: Message):
    await message.answer('Наші товари: ', reply_markup=kb.catalog)


@dp.callback_query(F.data == 'Bitcoin')
async def cb_bitcoin(callback: CallbackQuery):
    await callback.answer(f'Ви обрали {callback.data}', show_alert=True)
    await callback.message.answer(f'Ви обрали {callback.data}')


@dp.callback_query(F.data == 'Ethereum')
async def cb_eth(callback: CallbackQuery):
    await callback.answer(f'Ви обрали {callback.data}', show_alert=True)
    await callback.message.answer(f'Ви обрали {callback.data}')


@dp.callback_query(F.data == 'Dogecoin')
async def cb_doge(callback: CallbackQuery):
    await callback.answer(f'Ви обрали {callback.data}', show_alert=True)
    await callback.message.answer(f'Ви обрали {callback.data}')


# Обробник інформації
@dp.message(F.text == 'Інформація')
async def inform(message: Message):
    await message.answer('Інформація про бота...'
                         'Тут може бути що завгодно', reply_markup=kb.inform)


# @dp.message() Відповідає користувачеві на будь-які дії, крім команд.
# Повинен використовуватися завжди в кінці, інакше інші не спрацюють
@dp.message()
async def echo(message: Message):
    await message.answer('Будьласька, оберіть команду')


# Нескінченна робота бота
async def main():
    await dp.start_polling(bot)

# Дефолт фукція
if __name__ == '__main__':
    # Обробка вийняків
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот завершил работу.')
