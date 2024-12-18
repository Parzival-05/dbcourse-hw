from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from config import DBConnectionConfig

engine = create_engine(DBConnectionConfig.connection_string, echo=False)
session_maker = sessionmaker(bind=engine)
db_session = session_maker()


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
