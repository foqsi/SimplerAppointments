from app import db
from flask_login import UserMixin

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), unique=True, nullable=False)
    address = db.Column(db.String(250), nullable=True)
    state = db.Column(db.String(250), nullable=True)
    zip_code = db.Column(db.String(250), nullable=True)
    country = db.Column(db.String(250), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="employee")
    
    # Relationships
    company = db.relationship('Company', backref=db.backref('users', lazy=True))
    company_appointments = db.relationship('Appointment', backref='user', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    client_fname = db.Column(db.String(150), nullable=False)
    client_lname = db.Column(db.String(150), nullable=False)
    client_email = db.Column(db.String(150), nullable=False)
    client_phone = db.Column(db.String(15), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Scheduled")

    # Updated relationship
    client = db.relationship('User', backref='client_appointments', lazy=True)
