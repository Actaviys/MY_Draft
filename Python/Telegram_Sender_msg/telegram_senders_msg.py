import telegram_send
import asyncio

async def main():
    await telegram_send.send(messages=["Hello"])
    await telegram_send.send(files=["screen.jpg"])
    

asyncio.run(main())  # Запускаємо асинхронну функцію