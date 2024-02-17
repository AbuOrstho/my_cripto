import time
import asyncio
import sys

# Предполагаем, что эти импорты относятся к вашим модулям и они уже адаптированы под асинхронный запуск
from Coinex.Coinex import coinex
from LBank.LBank import lbank
from BitMart.BitMart import bitmart
from Huobi.Huobi import huobi
from MEXC.MEXC import mexc


async def main():
    start_time = time.time()

    # Предполагаем, что run методы асинхронные и можно вызвать await на них
    await asyncio.gather(
        coinex.run(),
        lbank.run(),
        bitmart.run(),
        huobi.run(),
        mexc.run()
    )

    print(f"Время выполнения: {time.time() - start_time} секунд.")


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
