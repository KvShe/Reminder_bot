from create_bot import dp
from aiogram.utils import executor
from controller import on_startup


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    scheduler.start()
