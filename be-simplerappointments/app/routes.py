from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required, login_user
from flask_mail import Message
from app.models import db, User, Appointment, Company
from app import db, mail
from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy import Date
from sqlalchemy.exc import SQLAlchemyError

routes = Blueprint('routes', __name__)
bc = Bcrypt()

@routes.route('/')
def home():
    return "Welcome to Simpler Appointments!"

@routes.route('/register_company', methods=['POST'])
def register_company():
    try:
        data = request.json
        if not data or not all(key in data for key in ['company_name']):
            return jsonify({'message': 'Missing required field: name'}), 400
        
        company = Company(
            company_name=data['company_name'],
            address=data.get('address'),
            state=data.get('state'),
            zip_code=data.get('zip_code'),
            country=data.get('country'),
            phone_number=data.get('phone_number'),

        )
        db.session.add(company)
        db.session.commit()
        
        return jsonify({'message': 'Company registered successfully', 'company_id': company.id}), 201
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500


@routes.route('/register', methods=['POST'])
def register():
    try:
        data = request.json

        # Validate required fields
        required_fields = {'company_id', 'username', 'email', 'password'}
        missing_fields = required_fields - set(data.keys())
        if missing_fields:
            return jsonify({'message': 'Missing required fields', 'missing_fields': list(missing_fields)}), 400

        # Verify the company exists
        company = Company.query.get(data['company_id'])
        if not company:
            return jsonify({'message': 'Invalid company_id: Company does not exist'}), 400

        # Hash the password
        hashed_password = bc.generate_password_hash(data['password']).decode('utf-8')

        # Create the user
        user = User(
            company_id=data['company_id'],
            username=data['username'],
            email=data['email'],
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201

    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500



@routes.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and bc.check_password_hash(user.password, data['password']):
            login_user(user)
            return jsonify({"message": "Login successful"})
        return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500

# TODO: Add employees
@routes.route('/access', methods=['POST'])
@login_required  # Ensure the user is logged in
def add_employee():
    if current_user.role != "owner" or current_user.role != "admin":
        return jsonify({"message": "Only the owner and admins can add employees"}), 403
    
    data = request.json
    new_user = User(
        company_id=current_user.company_id,
        username=data['username'],
        email=data['email'],
        password=bc.generate_password_hash(data['password']).decode('utf-8'),
        role="assistant"
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Assistant added successfully"}), 201
 

@routes.route('/api/appointments', methods=['POST'])
def manage_appointments():
    try:
        data = request.json

        # Validate required fields
        required_fields = {'client_id', 'client_fname', 'client_lname', 'client_email', 'client_phone', 'date'}
        missing_fields = required_fields - set(data.keys())
        if missing_fields:
            return jsonify({'message': 'Missing required fields', 'missing_fields': list(missing_fields)}), 400

        # Validate client_id
        user = User.query.get(data['client_id'])
        if not user:
            return jsonify({'message': 'User not found'}), 404

        # Parse the date string
        appointment_date = datetime.fromisoformat(data['date'])

        # Create the appointment
        new_appointment = Appointment(
            client_id=data['client_id'],
            client_fname=data['client_fname'],
            client_lname=data['client_lname'],
            client_email=data['client_email'],
            client_phone=data['client_phone'],
            date=appointment_date,
            status="Scheduled"
        )
        db.session.add(new_appointment)
        db.session.commit()

        return jsonify({'message': 'Appointment created!', 'data': {
            'client_id': new_appointment.client_id,
            'client_fname': new_appointment.client_fname,
            'client_lname': new_appointment.client_lname,
            'client_email': new_appointment.client_email,
            'client_phone': new_appointment.client_phone,
            'date': new_appointment.date.isoformat(),
            'status': new_appointment.status
        }}), 201

    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500


@routes.route('/api/appointments/reschedule/<int:appointment_id>', methods=['PUT'])
def reschedule_appointment(appointment_id):
    try:
        data = request.json

        # Validate required fields
        if not data or 'new_date' not in data:
            return jsonify({'message': 'Missing required field: new_date'}), 400

        # Parse the new date
        try:
            new_date = datetime.fromisoformat(data['new_date'])
        except ValueError:
            return jsonify({'message': 'Invalid date format'}), 400

        # Find the appointment by ID
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'message': 'Appointment not found'}), 404

        # Update the appointment date and status
        appointment.date = new_date
        appointment.status = "Rescheduled"  # Change the status to 'Rescheduled'
        db.session.commit()

        return jsonify({
            "message": "Appointment rescheduled successfully",
            "data": {
                "appointment_id": appointment_id,
                "client_fname": appointment.client_fname,
                "client_lname": appointment.client_lname,
                "client_email": appointment.client_email,
                "client_phone": appointment.client_phone,
                "new_date": appointment.date.isoformat(),
                "status": appointment.status
            }
        }), 200

    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500

@routes.route('/api/appointments/cancel/<int:appointment_id>', methods=['PUT'])
def cancel_appointment(appointment_id):
    try:
        # Find the appointment by ID
        appointment = Appointment.query.get(appointment_id)
        if not appointment:
            return jsonify({'message': 'Appointment not found'}), 404

        # Update the status to "Cancelled"
        appointment.status = "Cancelled"
        db.session.commit()

        return jsonify({
            "message": "Appointment cancelled successfully",
            "data": {
                "appointment_id": appointment_id,
                "client_fname": appointment.client_fname,
                "client_lname": appointment.client_lname,
                "client_email": appointment.client_email,
                "client_phone": appointment.client_phone,
                "date": appointment.date.isoformat(),
                "status": appointment.status
            }
        }), 200

    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500


@routes.route('/api/appointments/<int:client_id>', methods=['GET'])
def get_appointments(client_id):
    try:
        user = User.query.get(client_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        appointments = Appointment.query.filter_by(client_id=client_id).all()
        return jsonify([{
            'client_fname': a.client_fname,
            'client_lname': a.client_lname,
            'client_email': a.client_email,
            'client_phone': a.client_phone,
            'date': a.date.isoformat(),
            'status': a.status
        } for a in appointments])
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500

@routes.route('/api/appointments', methods=['GET'])
def search_appointments():
    try:
        # Extract query parameters
        client_id = request.args.get('client_id', type=int)
        client_fname = request.args.get('client_fname')
        client_lname = request.args.get('client_lname')
        client_email = request.args.get('client_email')
        client_phone = request.args.get('client_phone')
        status = request.args.get('status')
        start_date = request.args.get('start_date')  # Range start date
        end_date = request.args.get('end_date')      # Range end date

        query = Appointment.query

        # Apply filters dynamically
        if client_id:
            query = query.filter(Appointment.client_id == client_id)
        if client_fname:
            query = query.filter(Appointment.client_fname.ilike(f"%{client_fname}%"))
        if client_lname:
            query = query.filter(Appointment.client_lname.ilike(f"%{client_lname}%"))
        if client_email:
            query = query.filter(Appointment.client_email.ilike(f"%{client_email}%"))
        if client_phone:
            query = query.filter(Appointment.client_phone.ilike(f"%{client_phone}%"))
        if status:
            query = query.filter(Appointment.status.ilike(f"%{status}%"))
        if start_date and end_date:
            start_date_parsed = datetime.fromisoformat(start_date).date()
            end_date_parsed = datetime.fromisoformat(end_date).date()
            query = query.filter(Appointment.date.between(start_date_parsed, end_date_parsed))
        elif start_date:
            start_date_parsed = datetime.fromisoformat(start_date).date()
            query = query.filter(Appointment.date >= start_date_parsed)
        elif end_date:
            end_date_parsed = datetime.fromisoformat(end_date).date()
            query = query.filter(Appointment.date <= end_date_parsed)

        # Fetch results
        appointments = query.all()

        return jsonify({
            'message': 'Appointments retrieved successfully',
            'data': [{
                'client_id': a.client_id,
                'client_fname': a.client_fname,
                'client_lname': a.client_lname,
                'client_email': a.client_email,
                'client_phone': a.client_phone,
                'date': a.date.isoformat(),
                'status': a.status
            } for a in appointments]
        }), 200

    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400
    except SQLAlchemyError as e:
        return jsonify({'message': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500


@routes.route('/api/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        msg = Message(
            'Appointment Confirmation',
            sender='your_email@example.com',
            recipients=[data['client_email']]
        )
        msg.body = (
            f"Dear {data['client_fname']} {data['client_lname']}, "
            f"your appointment is confirmed for {data['date']}. "
            f"Contact us at {data.get('client_phone')} if needed."
        )
        mail.send(msg)
        return jsonify({"message": "Email sent!"}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while sending email', 'details': str(e)}), 500


@routes.route('/debug/companies', methods=['GET'])
def debug_companies():
    try:
        companies = Company.query.all()
        return jsonify({
            'message': 'Companies retrieved successfully',
            'data': [{
                'id': company.id,
                'name': company.company_name,
                'address': company.address,
                'state': company.state,
                'zip_code': company.zip_code,
                'country': company.country,
                'phone_number': company.phone_number
            } for company in companies]
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500


@routes.route('/debug/users', methods=['GET'])
def debug_users():
    try:
        users = User.query.all()
        return jsonify({
            'message': 'Users retrieved successfully',
            'data': [{
                'id': user.id,
                'company_id': user.company_id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
            } for user in users]
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500


@routes.route('/debug/appointments', methods=['GET'])
def debug_appointments():
    try:
        appointments = Appointment.query.all()
        return jsonify({
            'message': 'Appointments retrieved successfully',
            'data': [{
                'id': appointment.id,
                'client_id': appointment.client_id,
                'client_fname': appointment.client_fname,
                'client_lname': appointment.client_lname,
                'client_email': appointment.client_email,
                'client_phone': appointment.client_phone,
                'date': appointment.date.isoformat(),
                'status': appointment.status
            } for appointment in appointments]
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'details': str(e)}), 500
