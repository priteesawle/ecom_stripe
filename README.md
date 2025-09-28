# 🛒 Ecom_stripe

A simple Django e-commerce app with **Stripe Checkout (test mode)** integration.

Users can:

* View products with images
* Select quantities
* Buy products via Stripe
* Instantly see their **paid orders** on the same page

---

## ✨ Features

* Django 5 + Stripe Checkout
* Product listing with images
* Secure payment flow (test mode)
* **My Orders** section for purchased items
* Double charge prevention

---

## 🛑 How Double Charge is Prevented

* When a user clicks **Buy Now**, the button is immediately disabled and shows *“Processing...”*.
* The backend checks if a **Stripe Checkout Session** already exists for that order before creating a new one.
* This ensures the same order cannot be processed twice at the same time.

---

## ⚙️ Installation & Run

1. **Clone this repo**

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   Create a `.env` file in the root of your project:

   ```ini
   STRIPE_PUBLIC_KEY=pk_test_XXXXXXXXXXXXXXXXXXXXXXXX
   STRIPE_SECRET_KEY=sk_test_XXXXXXXXXXXXXXXXXXXXXXXX
   DJANGO_SECRET_KEY=your_django_secret_key_here
   DEBUG=True
   ```

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run server**

   ```bash
   python manage.py runserver
   ```

8. Open in browser → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 💳 Stripe Test Cards

Use the following Stripe test card to simulate payments:

* **Card Number:** `4242 4242 4242 4242`
* **Expiry Date:** Any future date
* **CVC:** Any 3 digits
* **ZIP:** Any 5 digits

---

## 🛠 Tech Stack

* **Backend:** Python / Django
* **Database:** SQLite (default, can use Postgres/MySQL)
* **Payments:** Stripe API
* **Frontend:** HTML, CSS, Bootstrap

---
