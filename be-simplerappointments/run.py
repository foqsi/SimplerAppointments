from app import create_app, db
from app.models import Company, User, Appointment
from datetime import datetime

app = create_app()

def populate_test_data():
    """Populate the database with test data."""
    # Check if there is already data in the database
    if not Company.query.first():  # Only populate if the database is empty
        # Create companies
        company1 = Company(company_name="Simpler Tech", address="123 Tech Lane", state="OK", zip_code="74008", country="USA", phone_number="4055551234")
        company2 = Company(company_name="Green Solutions", address="456 Green Way", state="OK", zip_code="74012", country="USA", phone_number="4055555678")
        company3 = Company(company_name="Tech Innovators", address="789 Innovation Blvd", state="OK", zip_code="74010", country="USA", phone_number="4055557890")
        company4 = Company(company_name="Tred Tech", address="1309 Leigh Circle", state="OK", zip_code="73099", country="USA", phone_number="4056401428")
        db.session.add_all([company1, company2, company3, company4])
        db.session.commit()

        # Create users
        user1 = User(company_id=company1.id, username="josh.longest", email="joshl@simplertech.com", password="hashedpassword1", role="owner")
        user2 = User(company_id=company1.id, username="liz.naneto", email="lizn@simplertech.com", password="hashedpassword2")
        user3 = User(company_id=company2.id, username="ed.davis", email="edd@greensol.com", password="hashedpassword3", role="owner")
        user4 = User(company_id=company2.id, username="robert.longest", email="robertl@greensol.com", password="hashedpassword4")
        user5 = User(company_id=company3.id, username="alice.cullen", email="alicec@techinnovators.com", password="hashedpassword5", role="owner")
        user6 = User(company_id=company3.id, username="bob.ross", email="bobr@techinnovators.com", password="hashedpassword6")
        user7 = User(company_id=company4.id, username="foqsi", email="foqsi03@gmail.com", password="dd107125", role="owner")
        db.session.add_all([user1, user2, user3, user4, user5, user6, user7])
        db.session.commit()

        # Create appointments
        appointment1 = Appointment(client_id=user1.id, client_fname="Edward", client_lname="Davis", client_email="edward.davis@client.com", client_phone="4056401428", date=datetime(2025, 1, 19, 10, 0))
        appointment2 = Appointment(client_id=user1.id, client_fname="Emma", client_lname="Stone", client_email="emma.stone@client.com", client_phone="4056401450", date=datetime(2025, 1, 20, 15, 30))
        appointment3 = Appointment(client_id=user2.id, client_fname="Carol", client_lname="Green", client_email="carolg@client.com", client_phone="4056401478", date=datetime(2025, 1, 21, 11, 0))
        appointment4 = Appointment(client_id=user3.id, client_fname="David", client_lname="Brown", client_email="davidb@client.com", client_phone="4056401489", date=datetime(2025, 1, 22, 14, 0))
        appointment5 = Appointment(client_id=user7.id, client_fname="Alice", client_lname="Smith", client_email="alice.smith@client.com", client_phone="4056401499", date=datetime(2025, 1, 23, 10, 30))
        appointment6 = Appointment(client_id=user7.id, client_fname="Bob", client_lname="Johnson", client_email="bob.johnson@client.com", client_phone="4056401500", date=datetime(2025, 1, 24, 16, 0))
        db.session.add_all([appointment1, appointment2, appointment3, appointment4, appointment5, appointment6])
        db.session.commit()

        print("Test data populated successfully!")

# Create database tables and populate test data
with app.app_context():
    db.drop_all()
    db.create_all()
    populate_test_data()  # Add test data only in development or when testing

if __name__ == '__main__':
    app.run(debug=True)
