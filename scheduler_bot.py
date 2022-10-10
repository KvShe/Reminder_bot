from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Dispatcher
from datetime import datetime, timedelta
from create_bot import dp
from database import read_from_database, del_reminder


scheduler = AsyncIOScheduler()


async def send_message_to_user(dp: Dispatcher, text, user_id):
    await dp.bot.send_message(text=text, chat_id=user_id)


# def scheduler_jobs():
#     # scheduler.add_job(send_message_to_admin, "interval", seconds=1, args=(dp,))
#     scheduler.add_job(send_message_to_admin, "date",
#                       run_date=datetime.now() + t, args=(dp,),
#                       timezone='Europe/Moscow')


async def adding_reminder_to_scheduler():
    for item in read_from_database():
        interval = timedelta(seconds=int(item[0]))
        scheduler.add_job(send_message_to_user, "date",
                          run_date=datetime.now() + interval, args=(dp, item[1], item[2]),
                          timezone='Europe/Moscow')
        del_reminder(item[3])
