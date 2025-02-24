import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# 🔹 Введи свій Telegram API Token
TOKEN = "YOUR_BOT_TOKEN"

# Ініціалізуємо бота та диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 📥 Обробка команди /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привіт! Я отримую команди з чату та консолі.")

# 📥 Обробка будь-якого повідомлення (ехо-відповідь)
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Ти написав: {message.text}")

# 📥 Очищення чату (команда /clear)
@dp.message(Command("clear"))
async def clear_chat(message: Message):
    chat_id = message.chat.id
    message_id = message.message_id

    for msg_id in range(message_id, message_id - 50, -1):
        try:
            await bot.delete_message(chat_id, msg_id)
        except Exception:
            pass

    await message.answer("✅ Чат очищено!")

# 📤 Функція для відправки повідомлення з консолі
async def send_console_message():
    chat_id = 14322222219339
    
    while True:
        text = input("Введіть повідомлення для відправки: ")
        if text.lower() in ["exit", "quit"]:
            print("❌ Вихід з консолі...")
            break
        try:
            await bot.send_message(chat_id, text)
            print(f"✅ Повідомлення відправлено: {text}")
        except aiogram.exceptions.TelegramAPIError as e:
            print(f"❌ Помилка: {e}")

# 🔹 Запуск бота та консолі одночасно
async def main():
    console_task = asyncio.create_task(send_console_message())
    bot_task = dp.start_polling(bot)
    await asyncio.gather(console_task, bot_task)

if __name__ == "__main__":
    asyncio.run(main())