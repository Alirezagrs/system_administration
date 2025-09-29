from datetime import date

from sqlalchemy import select

from db.config import create_session
from db.models import Customers

def get_guys_by_date(year, month, day):
    with create_session() as session:
        guys = session.execute(
            select(Customers).where(
                Customers.date==date(year,month,day)
            )
        )
        result = guys.all()
        return result

