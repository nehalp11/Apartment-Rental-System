<h1 align="center">🏢 Apartment & Rental Management System</h1>

<p align="center">
  <b>A Database-Driven Web Application for Managing Apartment Rentals</b><br>
  <i>List apartments, track availability, manage tenants and rental agreements</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-00000F?style=flat&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/Status-Completed-green?style=flat"/>
</p>

---

## 📌 About the Project

A relational database-driven web application built with **Flask and MySQL** for managing apartment rentals and tenant information. Property owners can list apartments, track availability, and manage rental agreements — all through a clean web interface.

Built as a **group project (2 members)** from **September to November 2025**.

---

## ✨ Features

### For Property Owners
- 🏠 List apartments with details (size, rent, location, amenities)
- 📊 Track availability status in real time
- 📝 Manage rental agreements digitally
- 👥 View and manage tenant information

### For Tenants
- 🔍 Browse available apartments
- 📋 View apartment details and pricing
- 📅 Track rental history and payment records

### Database Features
- ✅ Fully normalized tables (1NF, 2NF, 3NF)
- 🔑 Primary and foreign keys for data integrity
- 💾 Efficient storage of tenant, rental, and payment records

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python + Flask |
| Database | MySQL |
| Frontend | HTML, CSS, JavaScript |
| ORM | Flask-MySQLdb / raw SQL |
| Templating | Jinja2 |

---

## 🗄️ Database Schema

```
┌─────────────────┐       ┌─────────────────┐
│    APARTMENTS   │       │     TENANTS     │
├─────────────────┤       ├─────────────────┤
│ apartment_id PK │       │ tenant_id PK    │
│ owner_id FK     │       │ name            │
│ address         │       │ email           │
│ rent_amount     │       │ phone           │
│ bedrooms        │       │ id_proof        │
│ is_available    │       └────────┬────────┘
│ amenities       │                │
└────────┬────────┘                │
         │                         │
         └──────────┬──────────────┘
                    │
         ┌──────────▼──────────┐
         │   RENTAL_AGREEMENTS │
         ├─────────────────────┤
         │ agreement_id PK     │
         │ apartment_id FK     │
         │ tenant_id FK        │
         │ start_date          │
         │ end_date            │
         │ monthly_rent        │
         │ status              │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │     PAYMENTS        │
         ├─────────────────────┤
         │ payment_id PK       │
         │ agreement_id FK     │
         │ amount              │
         │ payment_date        │
         │ payment_method      │
         │ status              │
         └─────────────────────┘
```

---

## 📁 Project Structure

```
Apartment-Rental-System/
│
├── app.py                    # Main Flask application
├── config.py                 # Database configuration
├── requirements.txt          # Python dependencies
│
├── templates/                # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── apartments.html
│   ├── apartment_detail.html
│   ├── tenants.html
│   ├── agreements.html
│   └── payments.html
│
├── static/                   # CSS, JS, images
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── database/
│   └── schema.sql            # Database creation script
│
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- pip

### Steps

```bash
# Clone the repository
git clone https://github.com/nehalp11/Apartment-Rental-System.git
cd Apartment-Rental-System

# Install dependencies
pip install -r requirements.txt

# Set up the database
mysql -u root -p < database/schema.sql

# Configure database connection in config.py
# Update MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

# Run the application
python app.py
```

Visit **http://localhost:5000** in your browser.

---

## 📦 Requirements

```
Flask==2.3.0
Flask-MySQLdb==1.0.1
mysql-connector-python==8.0.33
Jinja2==3.1.2
```

---

## 🎯 Key Learnings

- Designing **normalized relational databases** with proper constraints
- Building **CRUD operations** with Flask and raw SQL / ORM
- Using **Jinja2 templating** for dynamic web pages
- Implementing **foreign key relationships** across multiple tables
- Understanding **data integrity** with primary and foreign keys
- **Team collaboration** — version control with Git

---

## 👥 Team

| Name | Role |
|------|------|
| Nehal P | Backend (Flask) + Database design |
| Team Member 2 | Frontend (HTML/CSS/JS) |

**Duration:** September 2025 — November 2025

---

<p align="center">
  <i>Built with ❤️ using Flask + MySQL</i>
</p>
