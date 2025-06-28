import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.client import client
from app.database.models import init_models

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN')) # type: ignore
    dp = Dispatcher()
    dp.include_routers(router, client)
    dp.startup.register(startup)
    await dp.start_polling(bot)

async def startup(dispatcher: Dispatcher):
    await init_models()
    logging.info('Бот запущен ...')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот выключен')