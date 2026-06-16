# 🛍️ OnlineBazar - E-Commerce Platform

> A feature-rich, full-stack e-commerce platform built with Django. Engineered for scalability, performance, and user experience.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.0%2B-darkgreen?style=flat-square&logo=django)
![PostgreSQL](https://img.shields.io/badge/Database-SQLite-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Database Models](#database-models)
- [User Roles & Permissions](#user-roles--permissions)
- [Core Functionalities](#core-functionalities)
- [Advanced Features](#advanced-features)
- [Configuration](#configuration)
- [Development](#development)
- [Team](#team)

---

## 🎯 Project Overview

**OnlineBazar** is a comprehensive e-commerce platform that simulates a real-world marketplace like Amazon or Flipkart. It supports **multi-seller operations**, **ML-powered recommendations**, **intelligent pricing**, **chatbot support**, and **comprehensive analytics**.

### Why OnlineBazar?
- ✅ **Production-Grade Code** - Enterprise patterns, clean architecture
- ✅ **Multi-User System** - Buyers, Sellers, SuperAdmin with role-based access
- ✅ **AI/ML Integration** - Demand forecasting, fraud detection, personalization
- ✅ **Payment Integration** - Razorpay gateway for secure payments
- ✅ **Real-time Features** - Order tracking, live chatbot, notifications
- ✅ **Scalable Design** - Modular Django apps, reusable components

---

## ✨ Key Features

### 👥 **User Management**
- User registration with **OTP verification**
- Secure login with phone/email-based OTP
- User profile management with address management
- Account suspension for policy violations

### 🛒 **Shopping Features**
- Browse products by **10+ categories**
- Advanced search with **filters and sorting**
- Product comparison tool
- Shopping cart with persistent storage
- **Price alerts** for wishlist items
- Order tracking with **real-time status updates**
- Multiple payment methods (**COD, UPI, Debit Card, Net Banking**)

### 💳 **Payment System**
- **Razorpay integration** for secure payments
- Multiple payment options
- Automatic payment verification
- Transaction history and receipts
- Refund management

### 🎁 **Membership Program**
- **OnlineBazar Prime** membership tiers
- Monthly (₹199) and Yearly (₹999) plans
- Member benefits:
  - Reduced shipping charges
  - Exclusive discounts
  - Early access to sales

### 🏪 **Seller Dashboard**
- Complete seller management system
- Product upload with **multiple image support**
- Inventory management
- Order request handling (Accept/Reject)
- Delivery partner integration
  - Blue Dart, Delhivery, DTDC, Ecom Express, XpressBees, Shadowfax
- Sales analytics and performance metrics
- Dynamic pricing control
- Discount/promotion management

### 🤖 **Intelligent Chatbot**
- **AI-powered customer support** chatbot
- Knowledge base system with Q&A pairs
- Query classification and routing
- Escalation to sellers/superadmin for complex queries
- Pending question management
- Learning system that improves with every interaction
- Support for Product, Order, and General queries

### 📊 **Machine Learning Features**
1. **Demand Forecasting** - Predict next 30-day demand per category
2. **Dynamic Pricing** - Adjust prices based on demand, competitors, seasonality
3. **Fake Review Detection** - Identify and flag suspicious reviews
4. **Product Recommendations** - Personalized suggestions based on browsing/purchase history
5. **Sales Prediction** - Forecast monthly sales trends
6. **Regional Analysis** - Market analysis by region/state
7. **Stock Alerts** - Automated warnings for low inventory

### 💰 **Discount & Promotion Engine**
- Festival-based discounts
- Category-specific offers
- Flat and percentage discounts
- Time-bound promotions
- Coupon code management
- Maximum discount limits

### 📈 **Analytics Dashboard** (SuperAdmin)
- Real-time sales metrics
- Order analytics
- Revenue tracking
- User behavior analysis
- Fraud detection alerts
- Demand forecasts
- Performance dashboards

### 🛡️ **Return Management**
- User-initiated return requests
- Seller handling of returns
- Return status tracking
- Automatic refund processing
- Return history and analytics

### 📱 **Responsive Design**
- Mobile-friendly interface
- Bootstrap-based responsive layout
- Touch-optimized controls
- Fast loading on 3G+ networks

---

## 🔧 Technology Stack

### Backend
- **Framework**: Django 4.0+ (Python 3.9+)
- **Database**: SQLite (Production-ready with PostgreSQL)
- **ORM**: Django ORM
- **API**: RESTful views with Django templates

### Frontend
- **HTML5**, **CSS3**, **JavaScript**
- **Bootstrap 5** - Responsive UI framework
- **Crispy Forms** - Django form rendering
- **Vanilla JS** - DOM manipulation and interactivity

### Additional Technologies
- **Payment Gateway**: Razorpay API
- **Image Processing**: Pillow for image uploads
- **Environment Config**: Python Decouple
- **Machine Learning**: Scikit-learn compatible (modular ML)
- **CSV Export**: For analytics and reporting

### Development Tools
- Django Development Server
- SQLite3 / PostgreSQL
- Git version control
- Virtual Environment (venv)

---

## 🏛️ Architecture

### Modular Design
The application follows Django's **app-based architecture**:

```
OnlineBazar/
├── users/              # User authentication & profile management
├── seller/             # Seller management & operations
├── store/              # Product catalog & shopping features
├── payments/           # Payment processing
├── superadmin/         # Analytics & platform management
├── chatbot/            # AI chatbot & support
├── ml/                 # Machine learning features
└── ecommerce/          # Core Django project settings
```

### Design Patterns
- **MVC Architecture** - Models, Views, Templates
- **Separation of Concerns** - Each app handles specific domain
- **DRY Principle** - Reusable models, views, templates
- **Template Inheritance** - Base template with modular partials
- **Signal-based Actions** - Post-processing with Django signals

---

## 💻 Installation

### Prerequisites
```bash
Python 3.9 or higher
pip (Python package manager)
Virtual environment support
```

### Step 1: Clone & Setup Virtual Environment

**Windows:**
```bash
cd d:\Project\copy of the project (MatkaSur)\ecommerce_project
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
cd ecommerce_project
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Database Setup
```bash
# Create initial migrations
python manage.py makemigrations users
python manage.py makemigrations seller
python manage.py makemigrations store

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Step 4: Load Sample Data (Optional)
```bash
python seed_data.py
```

### Step 5: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

---

## 🚀 Running the Application

### Development Server

**Windows:**
```bash
setup.bat
```

**Linux/Mac:**
```bash
bash setup.sh
```

**Manual:**
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

### Default Credentials
```
SuperAdmin Dashboard: admin@ecommerce.com / Admin@123
Admin Panel: http://127.0.0.1:8000/admin/
```

### Production Deployment
```bash
# Collect all static files
python manage.py collectstatic

# Use a production WSGI server (Gunicorn)
pip install gunicorn
gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000
```

---

## 📂 Project Structure

```
ecommerce_project/
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── seed_data.py              # Sample data generator
│
├── ecommerce/                # Core Django project
│   ├── __init__.py
│   ├── settings.py           # Django configuration
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI configuration
│
├── users/                    # User management app
│   ├── models.py             # UserProfile, OTPVerification, BazarMembership
│   ├── views.py              # Authentication & profile views
│   ├── urls.py               # User routes
│   └── migrations/
│
├── seller/                   # Seller management app
│   ├── models.py             # Seller, SellerOrderRequest, SellerDiscount
│   ├── views.py              # Seller dashboard & operations
│   ├── urls.py               # Seller routes
│   ├── templatetags/         # Custom template filters
│   └── migrations/
│
├── store/                    # Product & shopping app
│   ├── models.py             # Product, Order, Discount, Review
│   ├── views.py              # Shopping, cart, checkout
│   ├── urls.py               # Store routes
│   ├── context_processors.py # Template context helpers
│   ├── templatetags/         # Custom filters (currency, rating)
│   └── migrations/
│
├── payments/                 # Payment processing
│   ├── models.py             # Payment models
│   ├── views.py              # Razorpay integration
│   └── urls.py               # Payment routes
│
├── superadmin/               # Analytics & management
│   ├── models.py             # Analytics models
│   ├── views.py              # Dashboard & reports
│   └── urls.py               # Admin routes
│
├── chatbot/                  # AI chatbot
│   ├── models.py             # ChatSession, ChatMessage, PendingQuestion
│   ├── brain.py              # Chatbot logic & NLP
│   ├── views.py              # Chat interface
│   ├── urls.py               # Chat routes
│   └── migrations/
│
├── ml/                       # Machine Learning modules
│   ├── demand_forecast.py    # 30-day demand prediction
│   ├── dynamic_pricing.py    # Price optimization
│   ├── fake_review_detector.py # Fraud detection
│   ├── recommendations.py    # Personalized suggestions
│   ├── sales_prediction.py   # Sales forecasting
│   ├── regional_analysis.py  # Market analysis
│   └── stock_alert.py        # Inventory warnings
│
├── static/                   # Static files
│   ├── css/
│   │   └── style.css         # Custom styles
│   ├── js/                   # JavaScript files
│   └── images/
│
├── media/                    # User-uploaded files
│   └── products/
│       └── images/           # Product images
│
└── templates/                # HTML templates
    ├── base.html             # Base template
    ├── partials/             # Reusable components
    ├── store/                # Shopping templates
    ├── seller/               # Seller templates
    ├── payments/             # Payment templates
    ├── superadmin/           # Admin templates
    ├── chatbot/              # Chat templates
    └── users/                # Auth templates
```

---

## 🗄️ Database Models

### User Model
```python
UserProfile
├── user_id (UUID)
├── name, email, phone_number
├── gender
├── address (full address fields)
├── is_active, suspension_reason
└── created_at

OTPVerification
├── phone_number
├── otp, purpose (login/register/reset)
├── is_used, expires_at

BazarMembership (Prime)
├── user (OneToOne)
├── plan (monthly/yearly)
├── status, start_date, end_date
└── auto_renew
```

### Product & Shopping Models
```python
Product
├── product_id (UUID)
├── seller (ForeignKey)
├── category (10+ categories)
├── price, stock_quantity
├── images, reviews
└── metadata (manufacturing, expiry dates)

Order
├── order_id (UUID)
├── user (ForeignKey)
├── items → OrderItem
├── payment_status, order_status
├── delivery_address
├── razorpay_payment_id
└── discount

OrderItem
├── product, quantity, price

Discount
├── code (unique)
├── type (flat/percent)
├── applicable_category, festival_name
├── valid_from/until
```

### Seller Models
```python
Seller
├── seller_id (UUID)
├── business details
├── is_blacklisted
└── ratings/reviews

SellerOrderRequest
├── order, seller, order_item
├── status (pending/accepted/rejected/shipped)
├── delivery_partner, tracking_id
└── timestamps
```

### Chatbot Models
```python
ChatSession → ChatMessage
├── ChatKnowledge (Q&A database)
└── PendingQuestion (escalations)
```

---

## 👤 User Roles & Permissions

### 1️⃣ **Customer (Buyer)**
- Browse & search products
- Add to cart & checkout
- Place orders with multiple payment options
- Track orders in real-time
- Write product reviews & ratings
- Compare products
- Set price alerts
- Request returns
- Chat with bot/seller
- Join Prime membership

### 2️⃣ **Seller**
- Manage products (CRUD operations)
- Upload product images
- Manage inventory
- Accept/Reject orders
- Choose delivery partners
- View sales analytics
- Manage dynamic pricing
- Create discounts
- Respond to customer queries
- Handle returns
- View performance metrics

### 3️⃣ **SuperAdmin**
- Platform-wide analytics
- User management (suspend/activate)
- Seller management (approve/blacklist)
- Discount & promotion management
- View all orders & transactions
- Manage chatbot knowledge base
- Access ML features
- Generate reports
- Fraud detection oversight
- System configuration

---

## 🎯 Core Functionalities

### 🛍️ Shopping Flow
```
Browse Products → Search/Filter → View Details → Add to Cart 
→ Apply Coupon → Checkout → Select Payment Method 
→ Payment Gateway → Order Confirmation → Track Order
```

### 🏪 Seller Operations
```
Register Seller → Upload Products → Wait for Orders
→ Order Request Received → Accept/Reject 
→ Select Delivery Partner → Update Tracking 
→ Delivery Complete → Get Payment
```

### 💬 Chatbot Interaction
```
User Question → Bot Analysis → Knowledge Base Match
→ IF Found: Respond / IF NOT: Escalate to Seller/SuperAdmin
→ Answer Provided → Save to Knowledge Base
```

### 💳 Payment Processing
```
Checkout → Select Payment Method → Razorpay Gateway
→ Payment Verification → Update Order Status
→ Send Confirmation Email → Notify Seller
```

---

## 🚀 Advanced Features

### 🤖 Machine Learning Pipeline

#### 1. Demand Forecasting
- Analyzes 6-month sales history per category
- Predicts next 30-day demand using linear regression
- Falls back to mock data if insufficient history
- Used for: Inventory planning, stock optimization

#### 2. Dynamic Pricing Engine
- Factors considered:
  - Current demand vs supply
  - Competitor pricing (if available)
  - Seasonality index
  - Seller rating & feedback
  - Promotional events
- Updates prices automatically

#### 3. Fake Review Detection
- Analyzes review patterns:
  - Review velocity (too many in short time)
  - Reviewer account age & pattern
  - Text similarity across reviews
  - Rating distribution anomalies
- Flags suspicious reviews for manual verification

#### 4. Personalized Recommendations
- Collaborative filtering based on:
  - Purchase history
  - Browsing behavior
  - Similar user preferences
  - Category affinity
- Shows relevant products in home & search results

#### 5. Sales Prediction
- Time series analysis
- Predicts monthly revenue trends
- Helps in resource allocation

#### 6. Regional Analysis
- Market performance by state/district
- Category popularity by region
- Regional pricing insights
- Supply chain optimization

#### 7. Stock Alert System
- Automatic low inventory warnings
- Predicts stockouts
- Suggests reorder quantities
- Notifies sellers proactively

### 🔐 Security Features
- Password hashing with Django's security
- OTP-based authentication
- CSRF protection on all forms
- SQL injection prevention (Django ORM)
- XSS protection in templates
- Secure payment gateway integration
- Session management

### 📧 Notifications
- Order confirmation emails
- Payment receipts
- Order status updates
- Return request notifications
- Inventory alerts to sellers
- Chatbot escalation alerts

---

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=db.sqlite3
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Razorpay Keys
RAZORPAY_KEY_ID=your-key-id
RAZORPAY_KEY_SECRET=your-key-secret

# AWS S3 (Optional)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
```

### Settings Reference
```python
# ecommerce/settings.py
- DEBUG = config('DEBUG', default=True, cast=bool)
- ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')
- DATABASES = SQLite3 (easily switch to PostgreSQL)
- INSTALLED_APPS = All Django apps
- MIDDLEWARE = Security & session middleware
```

---

## 🛠️ Development

### Creating New Features

#### 1. Add a New Model
```python
# app_name/models.py
class MyModel(models.Model):
    field = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### 2. Create Migrations
```bash
python manage.py makemigrations app_name
python manage.py migrate
```

#### 3. Add Views
```python
# app_name/views.py
from django.shortcuts import render
from .models import MyModel

def my_view(request):
    items = MyModel.objects.all()
    return render(request, 'template.html', {'items': items})
```

#### 4. Register URLs
```python
# app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('my-route/', views.my_view, name='my_view'),
]

# ecommerce/urls.py
path('app/', include('app_name.urls')),
```

### Running Tests
```bash
python manage.py test app_name
```

### Debugging
```bash
# Django debug toolbar
pip install django-debug-toolbar

# Logging
import logging
logger = logging.getLogger(__name__)
logger.info("Message")
```

---

## 📊 Database Migrations

### View Migration Status
```bash
python manage.py showmigrations
```

### Create New Migration
```bash
python manage.py makemigrations app_name
```

### Apply Migrations
```bash
python manage.py migrate
```

### Rollback Migration
```bash
python manage.py migrate app_name 0001
```

---

## 🔄 Common Operations

### Create Superuser
```bash
python manage.py createsuperuser
# Email: admin@example.com
# Password: SecurePassword123
```

### Access Django Admin
```
http://127.0.0.1:8000/admin/
```

### Clear Database
```bash
python manage.py flush
```

### Shell Access
```bash
python manage.py shell
>>> from users.models import UserProfile
>>> user = UserProfile.objects.first()
```

### Export Data
```bash
python manage.py dumpdata > backup.json
python manage.py loaddata backup.json
```

---

## 📱 API Endpoints & Features

### User Routes
- `/users/register/` - User registration
- `/users/login/` - OTP login
- `/users/profile/` - View/Edit profile
- `/users/orders/` - View orders

### Store Routes
- `/store/` - Home page
- `/store/products/` - Product listing
- `/store/product/<id>/` - Product detail
- `/store/cart/` - Shopping cart
- `/store/checkout/` - Checkout page
- `/store/search/` - Search products

### Seller Routes
- `/seller/register/` - Seller registration
- `/seller/dashboard/` - Seller dashboard
- `/seller/products/` - Manage products
- `/seller/orders/` - Order requests

### Admin Routes
- `/superadmin/dashboard/` - Analytics
- `/superadmin/users/` - User management
- `/superadmin/orders/` - Order management

### Chatbot Routes
- `/chatbot/chat/` - Chat interface
- `/chatbot/api/message/` - Send message

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Full-stack web development with Django
- ✅ Database design & optimization
- ✅ User authentication & authorization
- ✅ Payment gateway integration
- ✅ Machine learning implementation
- ✅ Responsive UI/UX design
- ✅ RESTful API concepts
- ✅ Security best practices
- ✅ Scalable architecture
- ✅ Real-world e-commerce patterns

---

## 🚨 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'users'`
**Solution:**
```bash
pip install -r requirements.txt
python manage.py migrate
```

### Issue: Static files not loading
**Solution:**
```bash
python manage.py collectstatic --clear --noinput
```

### Issue: Database locked
**Solution:**
```bash
# Remove .sqlite3-shm and .sqlite3-wal files
rm db.sqlite3-shm db.sqlite3-wal
```

### Issue: Port 8000 already in use
**Solution:**
```bash
python manage.py runserver 8001  # Use different port
```

### Issue: Migration conflicts
**Solution:**
```bash
python manage.py migrate --fake-initial
```

---

## 📚 Documentation & Resources

- [Django Official Docs](https://docs.djangoproject.com/)
- [Razorpay Payment Integration](https://razorpay.com/docs/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Python Best Practices](https://pep8.org/)

---

## 🤝 Contributing

### Code Style
- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and DRY

### Commit Messages
```
[FEATURE] Add user authentication
[BUGFIX] Fix cart calculation error
[DOCS] Update README with setup instructions
[REFACTOR] Clean up view logic
```

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💻 Team

**Project Developers:**
- **Ankit Sharma**  - Logic , ML Features
- **Niraj Kumar**  - Database Design, ML Features, Backend Logic, Team Lead
- **Aditiya Kumar**  - Frontend

**Institution:** [Patna University]  
**Program:** MCA (Master of Computer Applications)  
**Project Duration:** [3 Months]

---

## 🏆 Key Achievements

- ✨ **Full E-Commerce Platform** - Complete shopping experience
- 🤖 **AI Integration** - 7+ ML features for smart operations
- 💳 **Real Payment Gateway** - Razorpay integration
- 📊 **Advanced Analytics** - Comprehensive dashboards
- 🛡️ **Enterprise Security** - Production-ready security measures
- 📱 **Responsive Design** - Works on all devices
- 🎯 **User-Centric** - Intuitive interfaces for all user types

---

<div align="center">

### ⭐ If you find this project helpful, please give it a star!

**Made with ❤️ by the development team**

</div>
