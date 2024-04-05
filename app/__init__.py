from flask import Flask

a = 2

app = Flask(__name__)


from app.controller import routes