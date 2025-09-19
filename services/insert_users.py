from sqlalchemy import select

from db.config import create_session
from db.models import Users

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
                if user.name =="morteza":
                    user = Users(
                         name=name,
                         password=password,
                         is_superuser = False
                    )
                    session.add(user)
                    session.commit()

                else:
                    user = Users(
                         name=name,
                         password=password,
                         is_superuser = True
                        )
                    session.add(user)
                    session.commit()
