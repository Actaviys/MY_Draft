import asyncio
from aiogram import Bot
from aiogram.types import FSInputFile


TOKEN = "**********"
bot = Bot(token=TOKEN)


photo_send = FSInputFile("screen.jpg")  # Завантажуємо файл для відправки
async def send_message():
    recipient = "UserID"
    
    message = "Привіт \nЯк справи?"

    try:
        await bot.send_message(recipient, message)
        await bot.send_photo(recipient, photo=photo_send)
        print(f"✅ Повідомлення відправлено до {recipient}")
    except Exception as e:
        print(f"❌ Помилка: {e}")


if __name__ == "__main__":
    asyncio.run(send_message())

