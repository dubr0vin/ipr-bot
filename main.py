from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def handle_command_start(message: types.Message):
    await message.reply("Бот для получения оценки по ИПР. Автор: Дубровин Дмитрий\n"
                        "Доступные команды:\n"
                        "/start, /help\n"
                        "/command1\n"
                        "/command2\n"
                        "/command3\n"
                        "/command4\n"
                        "/command5\n")


@dp.message_handler(commands=['command1'])
async def handle_command_start(message: types.Message):
    await message.reply("Мне нужно 10 по ИПР")


@dp.message_handler(commands=['command2'])
async def handle_command_start(message: types.Message):
    await message.reply("2*2=4")


@dp.message_handler(commands=['command3'])
async def handle_command_start(message: types.Message):
    await message.reply("ИПР - лучший предмет")


@dp.message_handler(commands=['command4'])
async def handle_command_start(message: types.Message):
    await message.reply("Лол")


@dp.message_handler(commands=['command5'])
async def handle_command_start(message: types.Message):
    await message.reply("Кек")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
