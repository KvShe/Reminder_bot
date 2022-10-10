from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from database import add_remainder
import scheduler_bot


class StateHandler(StatesGroup):
    reminder = State()
    times = State()


async def reminder_loading(message: types.Message):
    await message.answer('О чём напомнить?')
    await StateHandler.reminder.set()  # установил состояние напоминания


async def reminder_times(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
        data['reminder'] = message.text
    await message.answer('Через сколько напомнить?')
    await StateHandler.next()


async def timer_launch(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['times'] = message.text
    add_remainder([data['user_id'], data['reminder'], data['times']])
    await message.answer('Напоминание создано')
    await scheduler_bot.adding_reminder_to_scheduler()
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reminder_loading, commands=['remind_me_through'], state=None)
    dp.register_message_handler(reminder_times, state=StateHandler.reminder)
    dp.register_message_handler(timer_launch, state=StateHandler.times)
