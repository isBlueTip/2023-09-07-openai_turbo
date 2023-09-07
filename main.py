# this is bot's entrypoint

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router


async def main():
    bot = Bot(token=config.TG_BOT_TOKEN, parse_mode=ParseMode.HTML)
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # todo find and verbatimize logs
    asyncio.run(main())
