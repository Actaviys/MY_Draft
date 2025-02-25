import asyncio
import telegram_send
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# 🔹 Встав свій Telegram API Token
TOKEN = ""

# Ініціалізація бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 📩 Функція для відправки повідомлення через telegram_send
async def send_message(text):
    await telegram_send.send(messages=[text])


# Функція для очищення всього чату
async def clear_chat(message: Message):
    chat_id = message.chat.id  # Отримуємо ID чату
    message_id = message.message_id  # Отримуємо ID останнього повідомлення
    
    for msg_id in range(message_id, message_id - 50, -1):  # Видаляємо останні 50 повідомлень
        try:
            await bot.delete_message(chat_id, msg_id)
        except Exception:
            pass  # Пропускаємо, якщо повідомлення не можна видалити
    
    await message.answer("✅ Чат очищено!")  # Відправляємо підтвердження




# 📥 Обробник команд:
@dp.message(Command("start")) # /start
async def start_handler(message: Message):
    await message.answer("Привіт! Надішли мені повідомлення, і я повторю його.")

@dp.message(Command("clear"))
async def clear_command(message: Message):
    await clear_chat(message)



# 📥 Обробник будь-якого повідомлення
@dp.message()
async def echo_message(message: Message):
    print(message.text)
    await message.answer(f"Ти надіслав: {message.text}")  # Відповідь користувачу
    await send_message(f"Бот отримав повідомлення: {message.text}")  # Надсилаємо лог у telegram_send



# 🔹 Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())