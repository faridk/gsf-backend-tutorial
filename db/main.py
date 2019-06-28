from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


database_url = "sqlite:///data/database.sqlite3"
db_engine = create_engine(database_url, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))
Base = declarative_base()
Base.query = db_session.query_property()
# Has to be below Base intialization since User imports it
from db.models import User


def init_db():
    Base.metadata.drop_all(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)

    admin = User(email="admin@domain.com", password="2SxUJUYTFtid5UzoQ6xRmWBixDGgRx")
    db_session.add(admin)
    db_session.commit()