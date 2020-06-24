import asyncio

from aiogram import executor

from config import admin_id
from load_all import bot, create_db


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    # Подождем пока запустится база данных...
    await asyncio.sleep(10)
    await create_db()
    await bot.send_message(admin_id, "Я запущен!")


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
