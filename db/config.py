from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

url = 'sqlite:///hefa_data.db'


@lru_cache(maxsize=32)
def engine():
    _engine = create_engine(url=url)
    return _engine


def create_session() -> Session:
    session = sessionmaker(
        bind=engine(), autoflush=False, expire_on_commit=False
        )
    return session()
