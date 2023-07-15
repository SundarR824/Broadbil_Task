from flask import Flask
from flask_jwt_extended import JWTManager
from app.configs import Configs, DatabaseConfigs

app = Flask(__name__)
app.config.from_object(Configs)

jwt = JWTManager(app)

from app.routes import routes

app.register_blueprint(routes.bp)
