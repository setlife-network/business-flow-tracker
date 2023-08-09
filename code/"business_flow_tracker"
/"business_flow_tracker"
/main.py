from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initialize Flask
app = Flask(__name__)

# Set secret key
app.config['SECRET_KEY'] = 'your-secret-key'

# Set database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize LoginManager
login_manager = LoginManager(app)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Import routes
from business_flow_tracker import routes
