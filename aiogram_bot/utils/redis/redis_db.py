import aioredis

from loader import scheduler

redis = aioredis.from_url(
    "redis://18.191.9.118", port=6379, decode_responses=True
)


async def redis_write(name, value):
    await redis.set(name, value)


async def redis_get():
    date_h = await redis.get('date_h')
    date_m = await redis.get('date_m')

    usd_b = await redis.get('usd_b')
    usd_s = await redis.get('usd_s')
    eur_b = await redis.get('eur_b')
    eur_s = await redis.get('eur_s')
    chf_b = await redis.get('chf_b')
    chf_s = await redis.get('chf_s')

    temp_city = await redis.get('temp_city')
    wind_spd = await redis.get('wind_spd')
    hmdt = await redis.get('hmdt')
    weather_desc = await redis.get('weather_desc')

    btc = await redis.get('btc')
    eth = await redis.get('eth')
    sol = await redis.get('sol')
    bnb = await redis.get('bnb')
    return date_h, date_m, temp_city, weather_desc, hmdt, wind_spd, usd_b, usd_s, eur_b, eur_s, chf_b, chf_s, btc, eth, sol, bnb


def redis_update():
    scheduler.add_job(redis_get, 'interval', seconds=60)
