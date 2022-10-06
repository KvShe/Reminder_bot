from aiogram import types, Dispatcher
from create_bot import bot


# @dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}!\n'
                                                 'Я твой тестовый бот'.format(message.from_user))
    print(message.from_user)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
