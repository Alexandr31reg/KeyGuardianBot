import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.handlers import router

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN')) # type: ignore
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        print('Бот включен')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')