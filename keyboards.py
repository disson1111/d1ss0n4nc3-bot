from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🆕 открыть карточку")
        ],
        [
            KeyboardButton(text="🧑‍🧑‍🧒‍🧒 collection")
        ],
        [
            KeyboardButton(text="👤 профиль")
        ]
    ],
    resize_keyboard=True
)


again_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="ешо хочу",
                callback_data="open_again"
            )
        ]
    ]
)
