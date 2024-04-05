import os
import logging

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

host = os.getenv("RDS_ENDPOINT")
user = os.getenv("RDS_USER")
pw = os.getenv("RDS_PASSWORD")
db_name = os.getenv("RDS_DB")

db_url = rf"mysql+pymysql://{user}:{pw}@{host}:{3306}/{db_name}?charset=utf8mb4"

engine = create_engine(
    db_url,
    pool_size=256,
    max_overflow=128,
    pool_recycle=240,
    pool_pre_ping=True,
    connect_args={"connect_timeout": 10},
)


def get_session():
    session = db.session
    yield session

    try:
        session.commit()
        logging.debug("commit finished")
    except Exception as e:
        session.rollback()
        logging.error(f"commit error {e}")
    finally:
        session.close()
        logging.debug("session closed")


session = next(get_session())
