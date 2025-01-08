from app import db, create_app
from app.models import Company, User, Appointment
from datetime import datetime

# Create the Flask app and push the app context
app = create_app()
app.app_context().push()

# Clear existing data and populate the database with test data
def populate_db():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create companies
    company1 = Company(company_name="Simpler Tech", address="123 Tech Lane", state="OK", zip_code="74008", country="USA", phone_number="4055551234")
    company2 = Company(company_name="Green Solutions", address="456 Green Way", state="OK", zip_code="74012", country="USA", phone_number="4055555678")
    company3 = Company(company_name="Tech Innovators", address="789 Innovation Blvd", state="OK", zip_code="74010", country="USA", phone_number="4055557890")

    db.session.add_all([company1, company2, company3])
    db.session.commit()

    # Create users for each company
    user1 = User(company_id=company1.id, username="john.doe", email="john.doe@example.com", password="hashedpassword1", role="owner")
    user2 = User(company_id=company1.id, username="jane.doe", email="jane.doe@example.com", password="hashedpassword2", role="employee")

    user3 = User(company_id=company2.id, username="mark", email="mark@greensol.com", password="hashedpassword3", role="owner")
    user4 = User(company_id=company2.id, username="susan", email="susan@greensol.com", password="hashedpassword4", role="employee")

    user5 = User(company_id=company3.id, username="alice", email="alice@techinnovators.com", password="hashedpassword5", role="owner")
    user6 = User(company_id=company3.id, username="bob", email="bob@techinnovators.com", password="hashedpassword6", role="employee")

    db.session.add_all([user1, user2, user3, user4, user5, user6])
    db.session.commit()

    # Create appointments for each user
    appointment1 = Appointment(client_id=user1.id, client_fname="Edward", client_lname="Davis", client_email="edward.davis@example.com", client_phone="4056401428", date=datetime(2025, 1, 19, 10, 0), status="Scheduled")
    appointment2 = Appointment(client_id=user2.id, client_fname="Emma", client_lname="Stone", client_email="emma.stone@example.com", client_phone="4056401450", date=datetime(2025, 1, 20, 15, 30), status="Scheduled")

    appointment3 = Appointment(client_id=user3.id, client_fname="Carol", client_lname="Green", client_email="carolg@client.com", client_phone="4056401478", date=datetime(2025, 1, 21, 11, 0), status="Scheduled")
    appointment4 = Appointment(client_id=user4.id, client_fname="David", client_lname="Brown", client_email="davidb@client.com", client_phone="4056401489", date=datetime(2025, 1, 22, 14, 0), status="Scheduled")

    appointment5 = Appointment(client_id=user5.id, client_fname="Alice", client_lname="Smith", client_email="alice.smith@client.com", client_phone="4056401499", date=datetime(2025, 1, 23, 10, 30), status="Scheduled")
    appointment6 = Appointment(client_id=user6.id, client_fname="Bob", client_lname="Johnson", client_email="bob.johnson@client.com", client_phone="4056401500", date=datetime(2025, 1, 24, 16, 0), status="Scheduled")

    db.session.add_all([appointment1, appointment2, appointment3, appointment4, appointment5, appointment6])
    db.session.commit()

    print("Test data populated successfully.")

# Populate the database
if __name__ == "__main__":
    populate_db()
