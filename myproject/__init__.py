import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)

# Set secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')

# Database configuration
DATABASE_URL = "postgresql://khidmat_db_user:hJdPNpbLOHz6hX9ih8vZnDMOm7stkIXW@dpg-ctd89o1u0jms73f46vd0-a/khidmat_db"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
Migrate(app, db)

# Setup login manager
login_manager.init_app(app)
login_manager.login_view = "login"