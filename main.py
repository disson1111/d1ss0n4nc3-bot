import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from keyboards import main_keyboard, again_keyboard
from database import create_user, get_user, update_user
from handlers import router

async def main():

    bot = Bot(
        token=BOT_TOKEN
    )

    dp = Dispatcher()
    dp.include_router(router)

    @dp.message()
    async def test(message):

        if message.text == "/стартуем":

            create_user(message.from_user.id)

            await message.answer(
                "здарова маратик, это d1ss0n4nc3\n\n"
                "ботяра, в котором ты можешь открывать карточки с нишевыми персонажами, "
                "собирать свою тоталли факинг коллекшен и искать самых конч экземплярчиков\n\n"
                "редкость:\n\n"
                "🔵 COMMON\n"
                "🟢 RARE\n"
                "🟣 EPIC\n"
                "🔴 MYTHIC\n"
                "🟡 LEGENDARY\n\n"
                "удаче👅",
                reply_markup=main_keyboard
            )


    print("d1ss0n4nc3 запущен")

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
