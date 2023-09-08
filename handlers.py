from pprint import pprint

from aiogram import Router, flags
from aiogram.filters import Command
from aiogram.types import Message

import text_constants as text
import utils

router = Router()


@router.message(Command("start"))
async def start_command_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name))


@router.message()
@flags.chat_action("typing")
async def generate_text_response(msg: Message):
    message = await msg.answer(text.generation_waiting)
    if msg.text:
        prompt = msg.text
    elif msg.voice:  # todo transcribe audio
        return await message.edit_text(text.voice_error)
    else:
        return await message.edit_text(text.generation_error)

    print("")
    print("")
    pprint(f"msg voice = {msg.voice}")
    print("")
    print("")
    print(f"msg type = {type(msg)}")
    print("")
    print("")

    result = await utils.generate_text_response(prompt)
    if not result:
        return await message.edit_text(text.generation_error)
    await message.edit_text(result[0], disable_web_page_preview=True)


# @router.message(Gen.text_prompt)
# @router.message(F.audio)
# async def transcribe_voice_message(msg: Message, state: FSMContext):
#     audio = msg.audio
#
#     message = await msg.answer(text.generation_waiting)
#     result = await utils.generate_text_response(audio)
#     if not result:
#         return await message.edit_text(text.generation_error, reply_markup=kb.inline_exit_keyboard)
#     await message.edit_text(result[0], disable_web_page_preview=True)
