import aiohttp


async def get_url(currency):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url='https://api.binance.com/api/v3/ticker/price?symbol={}USDT'.format(currency.upper()),
                    ssl=False) as response:
                return float((await response.json())['price'])
    except KeyError:
        return None
