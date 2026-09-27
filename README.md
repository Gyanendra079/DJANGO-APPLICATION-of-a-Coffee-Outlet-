# ☕ BeanCraft

BeanCraft is a Django-based 24/7 coffee ordering web application built as a full-stack learning and portfolio project.

The application currently provides a coffee menu, shopping cart, checkout, order creation, order confirmation, order tracking, and Django Admin management.

---

## 🚀 Current Features

### Customer Features

- 🏠 Coffee shop homepage
- ☕ Dynamic coffee menu
- 📂 Product categories
- 🛒 Shopping cart
- ➕ Increase product quantity
- ➖ Decrease product quantity
- ❌ Remove products from cart
- 💳 Checkout form
- 📦 Order creation
- ✅ Order confirmation
- 🔎 Order tracking
- 📞 Contact page
- 📱 Responsive website design

### Admin Features

- Django Admin interface
- Manage menu items
- Enable/disable menu availability
- View customer orders
- View order items
- Update order status

### Current Order Statuses

- Received
- Preparing
- Ready
- Out for Delivery
- Completed
- Cancelled

---

# 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Backend | Django |
| Database | SQLite |
| Frontend | HTML5, CSS3, JavaScript |
| Authentication | Django Authentication |
| Version Control | Git |
| Repository | GitHub |

PostgreSQL, Django REST Framework, machine learning, and Generative AI are planned for later development.

---

# 🏗️ Project Architecture

```text
                        BeanCraft
                           |
             ┌─────────────┼─────────────┐
             |             |             |
           Home          Menu          Contact
                           |
                           v
                         Cart
                           |
                           v
                       Checkout
                           |
                           v
                         Order
                           |
              ┌────────────┴────────────┐
              |                         |
              v                         v
       Order Confirmation          Track Order
                                        |
                                        v
                                   Order Status