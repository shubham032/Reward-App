
# Django App Management System

This is a Django-based application where **admins** can add apps, set points, and manage user tasks, while **users** can complete tasks by uploading screenshots and earning points.

## 📌 Features

### ✅ Admin Panel (Custom, No Default Django Admin)

- Add, Edit, Delete Apps
- Assign Points to Apps
- View All User Submissions

### ✅ User Dashboard

- Signup & Login
- View Available Apps & Earn Points
- Upload Screenshots for Task Completion (Drag & Drop)
- View Profile & Earned Points

## 🚀 Setup & Installation

python -m venv venv
source venv/bin/activate # OnWindows:venv\Scripts\activate

## Install Dependencies

pip install -r requirements.txt

## Apply Migrations

python manage.py makemigrations
python manage.py migrate

## Run the Server

python manage.py runserver

## 🛠 Technologies Used

Django - Backend framework
Django REST Framework - API handling
Bootstrap - Frontend styling
SQLite (Default) - Database (Can be switched to PostgreSQL/MySQL)
JavaScript (Drag & Drop Uploads)


