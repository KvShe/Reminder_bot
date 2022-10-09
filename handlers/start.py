from aiogram import types, Dispatcher
from create_bot import bot
from datetime import date


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!\n'
                                                 f'Сегодня: {date.today()}\n'
                                                 'Я твой тестовый бот\n'
                                                 f'Твой id: {message.from_user.id}')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
