from sqlalchemy import Column, String
from db.main import Base

class User(Base):
    __tablename__ = "user"

    email = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = password