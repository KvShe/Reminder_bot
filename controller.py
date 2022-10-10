from aiogram.utils import executor
from create_bot import dp
from handlers import start, remind_through, when_to_remind
import scheduler_bot


start.register_handlers(dp)
remind_through.register_handlers(dp)
when_to_remind.register_handlers(dp)


async def on_startup(_):
    print('Bot online')


if __name__ == '__main__':
    scheduler_bot.scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
