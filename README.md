🧢 DRIFT KICKS — DJANGO ECOMMERCE SHOE STORE 👟

Drift Kicks is a full-fledged eCommerce website built using Django, a high-level Python web framework. It includes essential features such as user authentication, product browsing, cart management, checkout process, payment integration, and more. The website is designed to be robust, scalable, and user-friendly, providing a seamless shopping experience for customers.

📂 Table of Contents

Features

Technologies Used

Setup Instructions

Usage

Contributing

License

🚀 Features

🔐 User Authentication: Secure user registration, login, reset password, and profile management.

🛍️ Product Catalog: Browse and search products with detailed descriptions and images.

🛒 Shopping Cart: Add, update, and remove items from the cart seamlessly.

💳 Checkout Process: Smooth checkout flow with order summary and address management.

⚡ Payment Integration: Integrated with Razorpay for secure online payments.

📦 Order Management: View order history and status updates.

📱 Responsive Design: Mobile-friendly UI ensuring a consistent experience across devices.

🧑‍💼 Admin Panel: Manage products, orders, and users efficiently through Django's admin interface.

🛠️ Technologies Used

🐍 Django: Python-based web framework for backend development.

🧑‍🎨 HTML/CSS/JavaScript: Frontend development for a responsive and interactive UI.

🧾 Razorpay API: Payment gateway integration for secure transactions.

🎨 Bootstrap: Frontend framework for responsive design and UI components.

⚙️ Setup Instructions

To run this project locally, follow these steps:

Clone the repository:
git clone https://github.com/tejas7276/Drift-Kicks.git
cd Drift-Kicks

Create a virtual environment:
python -m venv venv

Activate the virtual environment:

On Windows: .\venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Note: Before running python manage.py migrate, create a .env file in your project root and update it using .env.example.
Add SECRET_KEY and DEBUG=True in your .env file.
To generate the SECRET_KEY:
Run django-admin shell and then:
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
Copy the key and paste it in your .env file.

Apply database migrations:
python manage.py migrate

Create a superuser (admin):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Open your browser and go to:
http://127.0.0.1:8000/

🧪 Usage

Admin Panel: Access the admin panel at http://127.0.0.1:8000/admin/ to manage products, orders, and users.

Shopping: Browse products, add items to the cart, proceed to checkout, and make payments using Razorpay.

Profile: Users can register, login, reset their password, view their order history, and update their profiles.

🤝 Contributing
Contributions are welcome! Please fork this repository and create a pull request with your proposed features, enhancements, or bug fixes.

📄 License
This project is licensed under the MIT License.

