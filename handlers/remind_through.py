from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
import db
import asyncio
from create_bot import bot


class StateHandler(StatesGroup):
    reminder = State()
    times = State()


async def reminder_loading(message: types.Message) -> None:
    await message.answer('О чём напомнить?')
    await StateHandler.reminder.set()  # установил состояние напоминания
    db.chat_id = message.chat.id


async def reminder_times(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['reminder'] = message.text
        # db.reminder[db.count] = data['reminder']
    await message.reply('Через сколько напомнить?')
    await StateHandler.next()


async def timer_launch(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['times'] = int(message.text)
    # db.times[db.count] = int(data['times'])
    await message.answer('Напоминание создано')

    await asyncio.sleep(data['times'])
    await bot.send_message(chat_id=message.from_user.id, text=data['reminder'])

    # now = datetime.now()
    # delta = now + timedelta(seconds=int(data['times']))
    # print(now, delta)

    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(reminder_loading, commands=['remind_me_through'], state=None)
    dp.register_message_handler(reminder_times, state=StateHandler.reminder)
    dp.register_message_handler(timer_launch, state=StateHandler.times)
