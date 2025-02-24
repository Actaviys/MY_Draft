import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def get_chat_id(message: types.Message):
    await message.answer(f"ID цієї групи: {message.chat.id}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())