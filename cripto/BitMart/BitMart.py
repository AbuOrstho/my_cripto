import json
import aiohttp
import asyncio


class BitMart:
    def __init__(self):
        # Загрузка данных из файла конфигурации
        self.web_data = json.load(
            open(r'url_lib.json', 'r',
                 encoding="UTF-8"))  # Укажите правильный путь к файлу
        self.base_url = self.web_data["BitMart"]["url"]
        self.all_tickers = self.web_data["BitMart"]["all_tickers"]
        self.all_name_tickers = self.web_data["BitMart"]["all_name_tickers"]
        self.ticker_price = self.web_data["BitMart"]["ticker_price"]
        self.commission = self.web_data["BitMart"]["commission"]
        self.urls = [self.all_name_tickers, self.all_tickers]

    async def fetch(self, session, url):
        """Асинхронный запрос к URL."""
        async with session.get(url) as response:
            print(f"Запрос к {url} завершен с кодом: {response.status}")
            data = await response.text()
            # Сохранение ответа в файл
            filename = fr"BitMart\response_{self.urls.index(url)}.json"
            with open(filename, 'w', encoding="UTF-8") as file:
                file.write(data)
                print(f"Данные сохранены в {self.urls.index(url)}")
            return data

    async def fetch_all(self):
        """Асинхронное выполнение всех запросов."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            await asyncio.gather(*tasks)

    def run(self):
        """Запуск асинхронной задачи."""
        asyncio.run(self.fetch_all())


# Использование класса для выполнения запросов и сохранения результатов
bitmart = BitMart()
bitmart.run()
