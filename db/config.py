from functools import lru_cache

from sqlalchemy import create_engine

url = 'sqlite:////_sqlite.db'


@lru_cache(maxsize=32)
def engine():
    _engine = create_engine(url=url)
    return _engine
