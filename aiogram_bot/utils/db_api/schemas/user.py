from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    full_name = Column(String(50))
    username = Column(String(50))
    bd_year = Column(Integer())
    bd_month = Column(Integer())
    bd_day = Column(Integer())

    query: sql.Select
