import os


from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("POSTGRES_USER"))
PGPASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
DATABASE = str(os.getenv("POSTGRES_DB"))
admins = [
    138874530
]

ip = os.getenv("ip")

db_host = str(os.getenv("DB_Host"))

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"
group_id = -1001489729427
# group_id = -1001423772208
