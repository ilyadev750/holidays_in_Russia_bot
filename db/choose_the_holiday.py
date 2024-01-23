from db.models import Holiday
from sqlalchemy import select
from sqlalchemy.orm import Session
from db.engine import engine

session = Session(bind=engine)


def get_the_result(holiday_name):
    info = select(Holiday).filter(Holiday.name.like(f'%%{holiday_name}%%'))
    result = session.scalars(info)
    return result







