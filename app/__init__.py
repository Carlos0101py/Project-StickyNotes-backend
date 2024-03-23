from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from app.controller import routes