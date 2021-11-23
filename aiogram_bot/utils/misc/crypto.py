from datetime import datetime

import aiohttp
import pytz

from bs4 import BeautifulSoup

from loader import scheduler
from utils.redis.redis_db import redis_write

usd = 'https://minfin.com.ua/currency/auction/usd/buy/kiev/'
eur = 'https://minfin.com.ua/currency/auction/eur/buy/kiev/'
chf = 'https://minfin.com.ua/currency/auction/chf/buy/all/'
currency = 'https://minfin.com.ua/currency/crypto/'
weather = "https://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=3152a27c5bc86b5d5891bd8b0d58e6ed"
crypto = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Csolana%2Cbinancecoin&vs_currencies=usd'


async def get_updates():
    async with aiohttp.ClientSession() as session:
        async with session.get(url= usd, ssl=False) as response:
            usd_b = BeautifulSoup(await response.text(), 'lxml').find('div', class_='buy').find('span', class_='Typography cardHeadlineL align').text[:5]
            usd_s = BeautifulSoup(await response.text(), 'lxml').find('div', class_='sale').find('span', class_='Typography cardHeadlineL align').text[:5]
            await redis_write('usd_b', usd_b)
            await redis_write('usd_s', usd_s)
        async with session.get(url=eur, ssl=False) as response:
            eur_b = BeautifulSoup(await response.text(), 'lxml').find('div', class_='buy').find('span', class_='Typography cardHeadlineL align').text[:5]
            eur_s = BeautifulSoup(await response.text(), 'lxml').find('div', class_='sale').find('span', class_='Typography cardHeadlineL align').text[:5]
            await redis_write('eur_b', eur_b)
            await redis_write('eur_s', eur_s)
        async with session.get(url=chf, ssl=False) as response:
            chf_b = BeautifulSoup(await response.text(), 'lxml').find('div', class_='buy').find('span', class_='Typography cardHeadlineL align').text[:5]
            chf_s = BeautifulSoup(await response.text(), 'lxml').find('div', class_='sale').find('span', class_='Typography cardHeadlineL align').text[:5]
            await redis_write('chf_b', chf_b)
            await redis_write('chf_s', chf_s)
        async with session.get(url=weather, ssl=False) as response:
            api_data = await response.json()
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_h = datetime.now(pytz.timezone("Europe/Kiev")).hour
            date_m = datetime.now().minute
            await redis_write('temp_city', round(temp_city, 2))
            await redis_write('weather_desc', weather_desc)
            await redis_write('hmdt', hmdt)
            await redis_write('wind_spd', wind_spd)
            await redis_write('date_h', date_h)
            await redis_write('date_m', date_m)
        async with aiohttp.ClientSession() as session:
            async with session.get(url=crypto, ssl=False) as response:
                api_data = await response.json()
                btc = api_data['bitcoin']['usd']
                eth = api_data['ethereum']['usd']
                sol = api_data['solana']['usd']
                bnb = api_data['binancecoin']['usd']
                await redis_write('btc', btc)
                await redis_write('eth', eth)
                await redis_write('sol', sol)
                await redis_write('bnb', bnb)


def crypto_values():
    scheduler.add_job(get_updates, 'interval', seconds=60)

