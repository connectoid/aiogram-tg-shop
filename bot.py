from aiogram import Bot, Dispatcher, types, executor

from settings import bot_config

bot = Bot(token=bot_config.bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message):
    markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Меню')
    btn2 = types.KeyboardButton('Корзина')
    btn3 = types.KeyboardButton('Заказы')
    btn4 = types.KeyboardButton('Новости')
    btn5 = types.KeyboardButton('Настройки')
    btn6 = types.KeyboardButton('Помощь')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    text = f'Привет {message.from_user.first_name}, вы запустили бот-магазин tg-shop'
    await message.answer(text, reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)