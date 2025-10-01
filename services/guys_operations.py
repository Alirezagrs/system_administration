from datetime import date

from sqlalchemy import select, and_

from db.config import create_session
from db.models import Customers

def get_guys_by_date(year, month, day):
    with create_session() as session:
        guys = session.execute(
            select(Customers).where(
                Customers.date==date(year,month,day)
            )
        )
        result = guys.scalars().all()
        return result

def admit_table_guys_changes(first_name,last_name,date,entrance_time,
                exit_time,work_with,gender,is_military,badge,organization):
    with create_session() as session:
        guy = Customers(
            first_name=first_name,
            last_name=last_name,
            date=date,
            entrance_time=entrance_time,
            exit_time=exit_time,
            work_with=work_with,
            gender=gender,
            is_military=is_military,
            badge=badge,
            organization=organization,
        )
        session.add(guy)
        session.commit()


def admit_table_guys_updates(first_name,last_name,date,entrance_time,
                exit_time,work_with,gender,is_military,badge,organization):
    with create_session() as session:
        guys = session.execute(
            select(Customers).where(
                and_(
                    Customers.first_name == first_name,
                    Customers.last_name == last_name,
                    Customers.date==date
                )
            )
        )
        result = guys.scalars().all()
        for guy in result:
            guy.first_name=first_name
            guy.last_name=last_name
            guy.date=date
            guy.entrance_time=entrance_time
            guy.exit_time=exit_time
            guy.work_with=work_with
            guy.gender=gender
            guy.is_military=is_military
            guy.badge=badge
            guy.organization=organization
        
        session.commit()