#!/usr/bin/env python
from db.main import db_session, init_db
from flask import Flask
from gql.schema import schema
from flask_graphql import GraphQLView
from flask_cors import CORS


app = Flask(__name__)
app.debug = True
# CORS
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

local = app.debug or ('FLASK_DEBUG' in os.environ and os.environ['FLASK_DEBUG'] == '1')
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, context={ 'client': '' }, graphiql= True if local else False))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    init_db()
    app.run()