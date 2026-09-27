# ☕ BeanCraft - Advanced Django Coffee E-Commerce & Cafe Management Web Application

**BeanCraft** is a feature-rich, high-performance web application built with Python and Django. It functions as both a premium online coffee store (e-commerce) and an automated cafe management system, offering a seamless experience for customers, baristas, and administrators alike.

## 🚀 Key Features

### 🛒 Customer & E-Commerce Features
* **Interactive Coffee Menu:** Browse gourmet coffee beans, brewing equipment, and fresh cafe items with advanced filtering (roast level, origin, price).
* **Smart Shopping Cart & Checkout:** Add products, apply coupon codes, and experience a smooth checkout flow.
* **Secure Payment Gateway:** Integrated with secure payment APIs (e.g., Stripe / PayPal / Razorpay) for safe transactions.
* **Real-time Order Tracking:** Customers can track their order status from "Brewing" to "Out for Delivery".
* **User Authentication & Profiles:** Secure sign-up, login (including social auth), password recovery, and personalized order history.

### 💼 Admin & Barista Dashboard (CMS)
* **Live Order Management:** Real-time updates for baristas to manage incoming cafe orders using AJAX/WebSockets.
* **Inventory Control System:** Automated alerts when coffee bean stocks or merchandise levels run low.
* **Sales Analytics & Reporting:** Visually track daily, weekly, and monthly revenue metrics via admin charts.
* **Dynamic Table Booking:** An automated reservation system for customers looking to book a table at the physical cafe.

## 🛠️ Tech Stack

* **Backend:** Python, Django Framework, Django REST Framework (DRF)
* **Database:** PostgreSQL (Production) / SQLite (Development)
* **Frontend:** HTML5, CSS3, JavaScript (ES6), Bootstrap 5, AJAX
* **Task Queue / Real-time:** Celery, Redis (for background email tasks and notifications)
* **Security:** Custom middleware, CSRF protection, secure password hashing, and environment variable masking

## 📦 Installation & Setup

Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd coffee-django-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your secret keys, database credentials, and payment API configurations.

5. **Run migrations and start the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Open `http://127.0.0` in your browser to view the app.

## 🔒 Security & Optimization
* Optimized SQL queries using `select_related` and `prefetch_related` to eliminate N+1 query problems.
* Implemented Django caching mechanisms for faster page load times on the menu and product listings.
