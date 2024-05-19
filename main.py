import asyncio
import logging

from config import TOKEN
from aiogram import Bot, Dispatcher
from handlers.private import private_router
from aiogram.enums import ParseMode
from download_music.music import music_router

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
dp.include_routers(private_router, music_router)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())