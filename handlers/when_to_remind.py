from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
import db
from create_bot import dp
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler1 = AsyncIOScheduler()


class StateHandler(StatesGroup):
    reminder1 = State()
    times1 = State()


async def reminder_loading(message: types.Message):
    await message.answer('О чём напомнить?')
    await StateHandler.reminder1.set()  # установил состояние напоминания
    db.chat_id = message.chat.id


async def reminder_times(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['reminder'] = message.text
    await message.answer('Когда напомнить?\n'
                         'Пример: 2022 10 30 16 00')
    await StateHandler.next()


async def timer_launch(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['times'] = list(map(int, message.text.split()))

    await message.answer('Напоминание создано')

    async def send_message_to_admin(dp: Dispatcher):
        await dp.bot.send_message(text=data['reminder'], chat_id=5196789047)

    scheduler1.add_job(send_message_to_admin, "date",
                       run_date=datetime(data['times'][0], data['times'][1], data['times'][2], data['times'][3],
                                         data['times'][4]), args=(dp,), timezone='Europe/Moscow')

    scheduler1.start()
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reminder_loading, commands=['when_to_remind'], state=None)
    dp.register_message_handler(reminder_times, state=StateHandler.reminder1)
    dp.register_message_handler(timer_launch, state=StateHandler.times1)
