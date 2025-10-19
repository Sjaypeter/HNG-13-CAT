HNG13-GetMeAPI
A simple Django REST API that returns my profile information along with a dynamic cat fact fetched from the Cat Facts API. This project was built as part of the HNG 13 Backend Wizards Stage 0 task.

🚀 Project Overview

Endpoint:

GET /me

Response Format:
{"status": "success", "user": {"email": "Sjaypeter.sjp@gmail.com", "name": "Peter Saint-John", "stack": "Python/Django"}, "timestamp": "2025-10-19T10:10:43.146896+00:00", "fact": "Researchers believe the word \u201ctabby\u201d comes from Attabiyah, a neighborhood in Baghdad, Iraq. Tabbies got their name because their striped coats resembled the famous wavy patterns in the silk produced in this city."}

status → always "success"

user → returns your name, email, and backend stack

timestamp → current UTC time (ISO 8601 format)

fact → random cat fact fetched from Cat Facts API

⚙ Setup Instructions (Run Locally)

1️⃣ Clone the Repository

git clone https://github.com/Sjaypeter/HNG-13-CAT cd HNG13-CAT

2️⃣ Create and Activate a Virtual Environment

python -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the root directory:

DJANGO_SECRET_KEY=your-secret-key DEBUG=True

⚠ Do not commit your .env file to GitHub.

5️⃣ Run Migrations

python manage.py migrate

6️⃣ Start the Development Server

python manage.py runserver

Visit: 👉 http://127.0.0.1:8000/me

🧩 Dependencies

Package Purpose

Django == 5.2.7 Web framework djangorestframework == 3.15.2 REST API support requests == 2.32.3 Fetches cat facts API gunicorn == 23.0.0 Production web server whitenoise == 6.7.0 Static file handling in production python-dotenv == 1.0.1 Environment variables management psycopg2-binary == 2.9.9 (optional) PostgreSQL driver for future use

Install all dependencies:

pip install -r requirements.txt

🌍 Environment Variables

Variable Description Example

DJANGO_SECRET_KEY Secret key for Django mysecretkey DEBUG Debug mode toggle True (local) / False (prod)

🧪 Testing the Endpoint

With Browser

Open:

http://127.0.0.1:8000/me

With cURL

curl http://127.0.0.1:8000/me

With Postman

Method: GET URL: http://127.0.0.1:8000/me

✅ You should receive a JSON response with your details and a random cat fact.

☁ Deployment

This API is deployed on Railway.app

Live URL: 👉 https://hng-13-cat-production.up.railway.app/me

🧠 What I Learned

How to create RESTful endpoints using Django REST Framework

How to consume third-party APIs in Django

Working with JSON responses

Managing environment variables securely

Preparing Django projects for production deployment on Railway

✨ Author

👨‍💻 Saint-John Peter 📧 sjaypeter.sjp@gmail.com 🧱 Stack: Python / Django 🔗 GitHub: Markmang

✅ Submission Checklist

[x] Working GET /me endpoint

[x] Dynamic Cat Fact Integration

[x] Deployed to Railway

[x] README with setup instructions

[x] Proper JSON response format

[x] All dependencies listed in requirements.txt