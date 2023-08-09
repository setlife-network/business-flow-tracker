from datetime import datetime
from business_flow_tracker import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    cashflows = db.relationship('CashFlow', backref='user', lazy=True)
    workflows = db.relationship('Workflow', backref='user', lazy=True)
    allocations = db.relationship('Allocation', backref='user', lazy=True)
    payments = db.relationship('Payment', backref='user', lazy=True)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)

class CashFlow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, amount: float, date: datetime, user: User):
        self.amount = amount
        self.date = date
        self.user = user

class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, description: str, date: datetime, user: User):
        self.description = description
        self.date = date
        self.user = user

class Allocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, amount: float, user: User):
        self.amount = amount
        self.user = user

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, amount: float, user: User):
        self.amount = amount
        self.user = user
