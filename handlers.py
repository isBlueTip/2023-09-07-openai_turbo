from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("я отвечу твоим id на любое сообщение")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"твой id :{msg.from_user.id}>")
