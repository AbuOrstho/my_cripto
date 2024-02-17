import time
import asyncio
import sys
from Coinex.Coinex import coinex
from LBank.LBank import lbank
from BitMart.BitMart import bitmart
from Huobi.Huobi import huobi
from MEXC.MEXC import mexc


start_time = time.time()

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Ваш код с использованием asyncio тут
coinex.run()
lbank.run()
bitmart.run()
huobi.run()
mexc.run()

print(time.time() - start_time)
