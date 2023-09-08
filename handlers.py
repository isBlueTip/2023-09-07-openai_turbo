from aiogram import F, Router, flags
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

import keyboards as kb
import text_constants as text
import utils
from states import Gen

router = Router()


@router.message(Command("start"))
async def start_command_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.main_menu)


@router.message(F.text == "назад в меню")
@router.message(F.text == "← назад в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.main_menu)


@router.callback_query(F.data == "generate_text_response")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.text_prompt)
    await clbck.message.edit_text(text.generate_text)
    await clbck.message.answer(text.gen_exit, reply_markup=kb.exit_keyboard)


@router.message(Gen.text_prompt)
@flags.chat_action("typing")
async def generate_text_response(msg: Message, state: FSMContext):
    prompt = msg.text
    message = await msg.answer(text.generation_waiting)
    result = await utils.generate_text_response(prompt)
    if not result:
        return await message.edit_text(text.generation_error, reply_markup=kb.inline_exit_keyboard)
    await message.edit_text(result[0], disable_web_page_preview=True)
