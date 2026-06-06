from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt





app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados_pinterest.db"
app.config["SECRET_KEY"] = "95d2314723cbce1c8410912f0e0d0af9"       # CHAVE DE SEGURANÇA
app.config["UPLOAD_FOLDER"]="static/fotos_posts"    # guarda a foto na pasta correta

database = SQLAlchemy(app)



bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "index"


from pinterest import views




