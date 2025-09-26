# GUI projects like tkinter and PYQT and ... are the best to know and comprehend so well OOP in python!!!!!!!!!!!!!!!!!!!!!!

### i did not used layout at first in login so the problem was if i wanted to use showFullScreen() the window has not been shown properly so i tried to use it ==> always use layout and frame.

### so important thing !!!!!!!! ===> you will be noticed after running and tsting your project that the first model you have designed have problems.you should fix it step by step.===> it was so important for me during testing the app. because at first i thouth that i should use update for editting the employee in tables but i found it would be replaced of that and it made mistakes during running. like:
    # first
    class EInfo(Base):
    __tablename__ = "employee_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[_date] = mapped_column(Date, nullable=True)
    entrance_time: Mapped[time] = mapped_column(Time, default=time(7,0,0))
    exit_time: Mapped[time] = mapped_column(Time, default=time(14,0,0))
    is_released: Mapped[str] = mapped_column(String(30), default="خیر")
    reseaon_of_releasing: Mapped[str] = mapped_column(nullable=True)
    mission_kind: Mapped[str] = mapped_column(nullable=True)
    mission_time: Mapped[time] = mapped_column(Time, nullable=True)
    overtime_work: Mapped[float] = mapped_column(nullable=True)

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id", ondelete="CASCADE",),
        unique=True)
    
    # later
    class EInfo(Base):
    __tablename__ = "employee_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[_date] = mapped_column(Date, nullable=True)
    entrance_time: Mapped[time] = mapped_column(Time, default=time(7,0,0))
    exit_time: Mapped[time] = mapped_column(Time, default=time(14,0,0))
    is_released: Mapped[str] = mapped_column(String(30), default="خیر")
    reseaon_of_releasing: Mapped[str] = mapped_column(nullable=True)
    mission_kind: Mapped[str] = mapped_column(nullable=True)
    mission_time: Mapped[time] = mapped_column(Time, nullable=True)
    overtime_work: Mapped[float] = mapped_column(nullable=True)

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id", ondelete="SET NULL",))
    
    fname_after_deleting: Mapped[str] = mapped_column(String(50))
    lname_after_deleting: Mapped[str] = mapped_column(String(50))
