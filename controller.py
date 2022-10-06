from aiogram.utils import executor
from aiogram import Dispatcher
from create_bot import dp, storage, bot
from handlers import start, remind_through, when_to_remind
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import db


scheduler = AsyncIOScheduler()


async def send_message_to_admin(dp: Dispatcher):
    await dp.bot.send_message(text=db.reminder[db.count], chat_id=5196789047)


def scheduler_jobs():
    # scheduler.add_job(send_message_to_admin, "interval", seconds=1, args=(dp,))
    scheduler.add_job(send_message_to_admin, "date",
                      run_date=db.t, args=(dp,),
                      timezone='Europe/Moscow')


start.register_handlers(dp)
remind_through.register_handlers(dp)
when_to_remind.register_handlers(dp)


async def on_startup(_):
    print('Bot online')


if __name__ == '__main__':
    # scheduler_jobs()
    # when_to_remind.scheduler_jobs()
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    scheduler.start()
    when_to_remind.scheduler1.start()
