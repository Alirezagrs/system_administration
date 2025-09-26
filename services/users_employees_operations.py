from datetime import date

from sqlalchemy import and_, select, delete

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
        employees = select(EInfo, Employees).join(
            Employees, Employees.id == EInfo.employee_id
        ).distinct()

        result = session.execute(employees)
        if result:
            res = result.all()
            return res


def get_employee(name, lname, badge):
    with create_session() as session:
        employees = select(Employees).where(
            and_(
                Employees.first_name == name,
                Employees.last_name == lname,
                Employees.badge == badge
            )
        )

        result = session.execute(employees)
        if result:
            res = result.scalar_one_or_none()
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
        

        










        # employee = select(Employees).where(
        #     and_(
        #         Employees.first_name == name,
        #         Employees.last_name == lname,
        #         Employees.badge == badge
        #     )
        # )
        # result = session.execute(employee)
        # emp_result = result.scalar_one_or_none()
        # if not emp_result:
        #     raise ValueError("کارمند پیدا نشد")

        # info = session.get(EInfo, emp_result.info_id)
        # if info:
        #     info.date = date
        #     info.entrance_time = entrance_time
        #     info.exit_time = exit_time
        #     info.is_released = is_released
        #     info.reseaon_of_releasing = reseaon_of_releasing
        #     info.mission_kind = mission_kind
        #     info.mission_time = mission_time
        #     info.overtime_work = overtime_work
        # session.commit()
