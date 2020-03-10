import os

from flask import Flask, request
from flask_migrate import Migrate

from graph import config
from graph.router import router_init
from graph.database import initialize_sql, Base

app = Flask(__name__)
app.config.from_object(config)

router_init(app)
initialize_sql()

migrate = Migrate(app, Base)
