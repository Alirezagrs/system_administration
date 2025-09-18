from functools import lru_cache

from sqlalchemy import create_engine

url = 'sqlite:////hafa_data.db'


@lru_cache(maxsize=32)
def engine():
    _engine = create_engine(url=url)
    return _engine
