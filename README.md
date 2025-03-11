
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

## Problem Set I - Regex

## Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list). {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

Solution:
import re
import json

data = '''{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'''

# Regex pattern to match numbers inside "id":<number>

pattern = r'"id":(\d+)'

# Extracting all numbers

numbers = re.findall(pattern, data)
numbers = list(map(int, numbers)) #Convert to integers

print(numbers) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 648, 649, 650, 651, 652, 653]

## Problem Set 3

## A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

solution:
For periodic tasks, Celery + Redis is a popular choice. Celery allows background task execution, and Redis serves as a broker.

Why Celery?
Scalable.
Reliable retry mechanisms.
Works well with Django.

## B. In what circumstances would you use Flask instead of Django and vice versa?

solutions:

When to Use Flask?
Lightweight API development.
Prototyping.

When to Use Django?
Full-stack applications.
Data-heavy apps with authentication.
