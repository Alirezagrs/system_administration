from datetime import date

from sqlalchemy import select, delete
from persiantools.jdatetime import JalaliDate

from db.config import create_session
from db.models import Users, Employees, EInfo


def create_user(name, password):
    with create_session() as session:
        if_user_exists = select(Users).where(
            Users.name == name,
        )
        if_user_exists = session.execute(if_user_exists)
        result = if_user_exists.scalar_one_or_none()

        if not result:
            user = Users(
                name=name
            )
            if user.name == "morteza":
                user = Users(
                    name=name,
                    password=password,
                    is_superuser=False
                )
                session.add(user)
                session.commit()

            else:
                user = Users(
                    name=name,
                    password=password,
                    is_superuser=True
                )
                session.add(user)
                session.commit()


def _create_employee(name, last_name, badge):
    with create_session() as session:
        today_date = JalaliDate.today()
        employee_info = EInfo()
        session.add(employee_info)
        session.commit()
        
        employee = Employees(
            first_name=name,
            last_name=last_name,
            badge=badge,
            info_id=employee_info.id
        )
        session.add(employee)
        session.commit()


def delete_employee(name, last_name, badge):
    with create_session() as session:
        employee = delete(Employees).where(
            Employees.first_name==name,
            Employees.last_name==last_name,
            Employees.badge==badge
        )
        session.execute(employee)
        session.commit()


def get_employees():
    with create_session() as session:
        employees = select(EInfo, Employees).join(
            Employees, Employees.info_id==EInfo.id
        )

        result = session.execute(employees)
        if result:
            res = result.all()
            return res 

def get_employees_by_date(year, month, day):
    with create_session() as session:
        employees = select(EInfo, Employees
        ).where(
            EInfo.date==date(year, month, day)
        ).join(
            Employees, EInfo.id==Employees.info_id
        )

        result = session.execute(employees)
        if result:
            res = result.all()
            return res 


def admit_table_changes():
    ...