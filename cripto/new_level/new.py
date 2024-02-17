import json
import aiohttp
import asyncio
import time

start_time = time.time()


async def fetch_price(session, url):
    """Асинхронный запрос к URL и возвращение результата."""
    async with session.get(url) as response:
        # Предполагаем, что ответ - это JSON
        response_json = await response.json()
        return f"Ответ от {url}: {response_json}"

async def main():
    # Загрузка данных из файла
    web_data = json.load(open('new.json', 'r', encoding="UTF-8"))

    b_name = web_data.keys()
    print(b_name)

    results = []  # Для сохранения результатов

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in b_name:
            print(url, web_data[url]["ticker_price"])
            for symbol in web_data[url]["coin"]:
                # Сформируем полный URL для каждого запроса
                full_url = web_data[url]["ticker_price"] + symbol
                # Добавляем задачу в список задач
                task = fetch_price(session, full_url)
                tasks.append(task)

        # Ожидаем выполнения всех задач и собираем результаты
        results = await asyncio.gather(*tasks)

    # Выводим собранные результаты
    for result in results:
        print(result)

# Запускаем асинхронный event loop
if __name__ == "__main__":
    asyncio.run(main())
print(time.time() - start_time)
