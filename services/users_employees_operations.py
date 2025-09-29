from datetime import date

from sqlalchemy import and_, select, delete, update

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
        employee = Employees(
            first_name=name,
            last_name=last_name,
            badge=badge,

        )
        session.add(employee)
        session.flush()
        
        employee_info = EInfo(
            employee_id=employee.id,
            fname_after_deleting = employee.first_name,
            lname_after_deleting = employee.last_name,

        )
        session.add(employee_info)
        session.commit()


def delete_employee(name, last_name, badge):
    # delete all records
    with create_session() as session:
        employee = delete(Employees).where(
            and_(
                Employees.first_name == name,
                Employees.last_name == last_name,
                Employees.badge == badge
            )
            
        )
        session.execute(employee)
        session.commit()


def get_employees():
    with create_session() as session:
        employee = select(Employees.first_name, Employees.last_name, Employees.badge).distinct()

        result = session.execute(employee)
        unique_employee = result.all()
        return unique_employee


def get_employee(name, lname, badge):
    with create_session() as session:
        employees = select(Employees.first_name, Employees.last_name, Employees.badge).where(
            and_(
                Employees.first_name == name,
                Employees.last_name == lname,
                Employees.badge == badge
            )
        ).distinct()

        result = session.execute(employees)
        if result:
            res = result.all()
            return res

def get_employees_by_date(year, month, day):
    with create_session() as session:
        employees = select(EInfo, Employees
        ).where(
            EInfo.date == date(year, month, day)
        ).join(
            Employees, EInfo.employee_id == Employees.id
        )

        result = session.execute(employees)
        if result:
            res = result.all()
            return res


def admit_table_changes(name, lname, badge, date, entrance_time, exit_time,
                        is_released, reseaon_of_releasing, mission_kind,
                        mission_time, overtime_work):
    with create_session() as session:
        # must not update you must create
        employee = Employees(
            first_name=name,
            last_name=lname,
            badge=badge,

        )
        session.add(employee)
        session.flush()

        employee_info = EInfo(
            date = date,
            entrance_time = entrance_time,
            exit_time = exit_time,
            is_released = is_released,
            reseaon_of_releasing = reseaon_of_releasing,
            mission_kind = mission_kind,
            mission_time = mission_time,
            overtime_work = overtime_work,
            employee_id = employee.id,
            fname_after_deleting = employee.first_name,
            lname_after_deleting = employee.last_name
        )
        session.add(employee_info)
        session.commit()
        

def admit_table_updates(name, lname, badge, date, entrance_time, exit_time,
                        is_released, reseaon_of_releasing, mission_kind,
                        mission_time, overtime_work):
    with create_session() as session:
        # must not update you must create
        emp = session.execute(
            select(Employees, EInfo).where(
                and_(
                    Employees.first_name == name,
                    Employees.last_name == lname,
                    Employees.badge == badge,
                    EInfo.date==date
                )
            ).join(
                EInfo, Employees.id==EInfo.employee_id
            )
        )

        result = emp.all()    
        for _, empinfo in result:
            empinfo.date = date
            empinfo.entrance_time = entrance_time
            empinfo.exit_time = exit_time
            empinfo.is_released = is_released
            empinfo.reseaon_of_releasing = reseaon_of_releasing
            empinfo.mission_kind = mission_kind
            empinfo.mission_time = mission_time
            empinfo.overtime_work = overtime_work

        session.commit()
  
