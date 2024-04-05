from dotenv import load_dotenv

load_dotenv(verbose=True, dotenv_path=".env")

import logging

from flask import Flask

from app.persistence.database import db, db_url
from app.commands.command import staiton_cli
from app.containers.repository_container import RepositoryContainer


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db.init_app(app)

app.container = RepositoryContainer()

logging.basicConfig(filename="app/logs/project.log", level=logging.DEBUG)

app.cli.add_command(staiton_cli)
