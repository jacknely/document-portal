from flask import Flask

from .models import db, dbinit
from .services import file_type, format_date_time
from .views import docs


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    with app.app_context():
        app.register_blueprint(docs)
        app.jinja_env.filters["format_date_time"] = format_date_time
        app.jinja_env.filters["file_type"] = file_type
        db.init_app(app)
        # dbinit(True)

    return app
