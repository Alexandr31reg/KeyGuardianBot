import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.client import client

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN')) # type: ignore
    dp = Dispatcher()
    dp.include_routers(router, client)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        print('Бот включен')
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот выключен')