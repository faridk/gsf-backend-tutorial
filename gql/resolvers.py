import random
import string
from db.main import db_engine, db_session
from db.models import User as UserModel

def login(email, password):
    # print(db_engine.execute('SELECT * FROM user').fetchall())
    queried_user = UserModel.query.filter_by(email=email).first()
    # Check if email belongs to a registered user
    if hasattr(queried_user, "email"):
        # Verify their password
        if password == queried_user.password:
            authToken = "authToken: " + "".join(random.choices(
                string.ascii_lowercase + string.digits, k=23))
            return authToken
        else: # Wrong password
            return "bad credentials"
    else: # User does NOT exist
        return "bad credentials"

def signup(email, password):
    # If email address is already in use
    if UserModel.query.filter_by(email=email).first() is not None:
        return "email in use"
    else:
        # Save new user record in the DB
        db_session.add(UserModel(email=email, password=password))
        db_session.commit()
        print('New user signup: %s '% email)
        authToken = "authToken: " + "".join(random.choices(
            string.ascii_lowercase + string.digits, k=23))
        return authToken