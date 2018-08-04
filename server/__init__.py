import flask

from server.utils import get_db


def register_blueprints(app):
    from server.routes import index
    app.register_blueprint(index)


def initialize_db():
    db = get_db(no_context=True)
    with open("db/db-structure.sql") as f:
        db_structure = f.read()
        db.executescript(db_structure)
    db.commit()


def create_app():
    app = flask.Flask(__name__)
    register_blueprints(app)
    initialize_db()
    return app
