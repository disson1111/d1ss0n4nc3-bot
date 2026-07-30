import json
import random
from datetime import date

from aiogram import Router, F
from aiogram.types import Message

from keyboards import main_keyboard, again_keyboard
from database import create_user, get_user, update_user


router = Router()


with open("cards.json", "r", encoding="utf-8") as file:
    cards = json.load(file)


RARITY_CHANCES = {
    "COMMON": 50,
    "RARE": 30,
    "EPIC": 10,
    "MYTHIC": 7,
    "LEGENDARY": 3
}


@router.message(F.text == "🆕 открыть карточку")
async def open_card(message: Message):

    create_user(message.from_user.id)

    user = get_user(message.from_user.id)

    today = str(date.today())


    if user["last_open"] == today:
        await message.answer(
            "седня всо мой маленки сиксевен🫰\n\n"
            "новая карточка будет доступна завтра"
        )
        return


    rarity = random.choices(
        list(RARITY_CHANCES.keys()),
        weights=list(RARITY_CHANCES.values())
    )[0]


    card = random.choice(cards)


    user["cards"].append(card["id"])
    user["last_open"] = today
    user["best_rarity"] = rarity

    update_user(
        message.from_user.id,
        user
    )


    await message.answer_photo(
        photo=card["image"],
        caption=f"""
ШО ЦЕ ТАКОЕ⁉️

⚜️карточка⚜️

нейм: {card['name']}

редкость: {rarity}

описание:
{card['description']}
""",
        reply_markup=again_keyboard
    )


@router.message(F.text == "👤 профиль")
async def profile(message: Message):

    user = get_user(message.from_user.id)

    await message.answer(
        f"""
❕карт собрано:
{len(user['cards'])}

💯 самая редкая:
{user['best_rarity']}
"""
    )


@router.message(F.text == "🧑‍🧑‍🧒‍🧒 collection")
async def collection(message: Message):

    user = get_user(message.from_user.id)

    await message.answer(
        f"""
COLLECTION:

❕всего карт:
{len(user['cards'])}

красава маратик🫰
"""
    )
