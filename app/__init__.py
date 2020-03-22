from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .services import file_type, format_date_time

# instantiate an instant of Flask named app
app = Flask(__name__)

app.secret_key = "56789dfbhj387dyhs"

# set filters to be used in jinja2 from services
app.jinja_env.filters["format_date_time"] = format_date_time
app.jinja_env.filters["file_type"] = file_type

app.config.from_object("settings")

db = SQLAlchemy(app)

from .views import *