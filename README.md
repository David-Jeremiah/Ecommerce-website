# 🛍️ Django ECommerce Website

A full-featured eCommerce web application built using Django. This project provides a solid foundation for an online store, including user authentication, product management, cart functionality, and order processing.

---

## 🚀 Features

- ✅ Product listing with categories
- ✅ Product detail pages
- ✅ Add to cart & checkout
- ✅ User registration and login
- ✅ Order management system
- ✅ Django admin panel
- ✅ Responsive front-end (HTML/CSS/Bootstrap)
- ✅ Secure authentication and form validation

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (easily swappable for PostgreSQL)
- **Tools:** Django Admin, Virtual Environment, Git/GitHub

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/David-Jeremiah/Ecommerce-website.git
   cd Ecommerce-website
2. Create and activate virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Run migrations
bash
Copy
Edit
python manage.py migrate

5. Create a superuser (admin)
bash
Copy
Edit
python manage.py createsuperuser

6.Start the development server
bash
Copy
Edit
python manage.py runserver

7. Visit http://127.0.0.1:8000/ to view the site.

🔐 Admin Panel
Access the Django admin dashboard at:

arduino
Copy
Edit
http://127.0.0.1:8000/admin/
Use the superuser credentials you created.

📁 Project Structure
csharp
Copy
Edit
Ecommerce-website/
├── ecommerce/            # Main Django app
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── db.sqlite3            # SQLite database
├── manage.py
├── requirements.txt
└── README.md
✅ Future Improvements
Payment gateway integration (e.g. Stripe, PayPal, MoMo)

Product reviews and ratings

Product filtering and search

Order confirmation emails

REST API support with Django REST Framework

🧑‍💻 Author
David Jeremiah
GitHub: @David-Jeremiah

📝 License
This project is open-source and available under the MIT License.

