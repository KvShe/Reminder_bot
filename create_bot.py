from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import token
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # класс хранит данные в оперативной памяти

storage = MemoryStorage()  # хранилище
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
