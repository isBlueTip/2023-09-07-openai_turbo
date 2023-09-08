from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu_layout = [
    [
        InlineKeyboardButton(text="Генерировать текст", callback_data="generate_text_response"),
    ],
    [
        InlineKeyboardButton(text="ещё кнопка 1", callback_data="buy_tokens"),
        InlineKeyboardButton(text="ещё кнопка 2", callback_data="balance"),
    ],
]

main_menu = InlineKeyboardMarkup(inline_keyboard=menu_layout)

exit_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="← назад в меню")]], resize_keyboard=True)

inline_exit_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="← назад в меню", callback_data="menu")]]
)
