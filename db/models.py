from datetime import date as _date, time

from sqlalchemy import String, ForeignKey, Date, Time, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, \
    MappedAsDataclass


class Base(DeclarativeBase):
    pass


class Users(Base):
    "those who work with software"
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    

class Employees(MappedAsDataclass, Base):
    __tablename__ = "employees"
    # can not use UniqueConstrait here. I get several same values by crating
    # with several date
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, init=False
    )
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    badge: Mapped[str] = mapped_column(String(50))
    


class EInfo(Base):
    __tablename__ = "employee_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[_date] = mapped_column(Date, nullable=True, unique=True)
    entrance_time: Mapped[time] = mapped_column(Time, default=time(7,0,0))
    exit_time: Mapped[time] = mapped_column(Time, default=time(14,0,0))
    is_released: Mapped[str] = mapped_column(String(30), default="خیر")
    reseaon_of_releasing: Mapped[str] = mapped_column(nullable=True)
    mission_kind: Mapped[str] = mapped_column(nullable=True)
    mission_time: Mapped[time] = mapped_column(Time, nullable=True)
    overtime_work: Mapped[float] = mapped_column(nullable=True)
    # foreignkey + unique = one to one relation
    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id", ondelete="SET NULL",),
        unique=True
    )
    fname_after_deleting: Mapped[str] = mapped_column(String(50))
    lname_after_deleting: Mapped[str] = mapped_column(String(50))


class Customers(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    date: Mapped[_date] = mapped_column(Date)
    entrance_time: Mapped[time] = mapped_column(Time)
    exit_time: Mapped[time] = mapped_column(Time)
    work_with: Mapped[int] = mapped_column(
        ForeignKey("employees.id", ondelete="CASCADE")
    )


class MilitaryGuy(Base):
    __tablename__ = "military_guys"
    id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE",),
        primary_key=True
    )
    badg: Mapped[str] = mapped_column(String(50))
    organization: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(15))


class NormalGuy(Base):
    __tablename__ = "normal_guys"
    id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"),
        primary_key=True
    )
    gender: Mapped[str] = mapped_column(String(15))
