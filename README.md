# Django Ecommerce REST API

Welcome to the Django Ecommerce REST API project! This is a robust, feature-rich backend for a modern e-commerce platform, built from the ground up with best practices in mind.

This repository serves as a practical showcase of modern Django development, focusing on clean code, security, scalability, and performance. It's an ideal foundation for building a real-world online store or for learning advanced Django and DRF concepts.

![Project Banner or Screenshot](https://placehold.co/800x400/2d3748/ffffff?text=Ecommerce%20Django%20API)

---

### ✨ Key Features

* **Custom User Model & Authentication:** A flexible authentication system built on a custom user model with email-based login.
* **Product Catalog Management:** A hierarchical system for managing products, categories, and target audiences (e.g., Men, Women, Kids).
* **Advanced Filtering & Search:** Powerful, performance-optimized product listing with support for filtering, searching, and ordering.
* **Dynamic Shopping Cart:** A fully functional cart system that supports both authenticated users and guest sessions.
* **RESTful API:** A clean and powerful API built with Django REST Framework.
* **Auto-generated API Documentation:** Interactive API documentation available with Swagger UI and ReDoc, powered by `drf-spectacular`.

---

### 🔧 Tech Stack

This project is built with a modern and scalable set of technologies:

* **Backend:**
    * [Python](https://www.python.org/)
    * [Django](https://www.djangoproject.com/)
    * [Django REST Framework](https://www.django-rest-framework.org/)
* **Database:**
    * Designed for MySql
* **Environment Management:**
    * [Miniconda / Conda](https://docs.conda.io/en/latest/miniconda.html)
* **API Documentation:**
    * [drf-spectacular](https://github.com/tfranzel/drf-spectacular)

---

### 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

#### Prerequisites

You must have Git and Miniconda (or Anaconda) installed on your system.

* [Miniconda Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

#### Installation Steps

1.  **Clone the Repository:**
    ```sh
    git clone [https://github.com/AhmedZhi10/e-commerce-django.git](https://github.com/AhmedZhi10/e-commerce-django.git)
    cd e-commerce-django
    ```

2.  **Create and Activate the Conda Environment:**
    This command uses the `environment.yml` file to create a new Conda environment with all the required packages.
    ```sh
    conda env create -f environment.yml
    ```
    After the environment is created, activate it:
    ```sh
    conda activate ecommerce_env 
    ```
    > **Note:** The environment name (`ecommerce_env`) is defined in the `environment.yml` file. Check the file if you need to confirm the name.

3.  **Set Up Environment Variables:**
    The project uses a `.env` file for sensitive settings. Rename the example file:
    ```sh
    # On Linux/macOS
    mv .env.example .env
    # On Windows
    rename .env.example .env
    ```
    Now, open the `.env` file and fill in the required values, especially the `SECRET_KEY`.

4.  **Apply Database Migrations:**
    This will create the necessary tables in your database.
    ```sh
    python manage.py migrate
    ```

5.  **Create a Superuser:**
    This account will give you access to the Django admin panel.
    ```sh
    python manage.py createsuperuser
    ```

6.  **Run the Development Server:**
    You're all set! Start the server:
    ```sh
    python manage.py runserver
    ```
    The application will be running at `http://127.0.0.1:8000`.

---

### 📚 API Documentation

Once the server is running, you can access the auto-generated API documentation at the following endpoints:

* **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
* **ReDoc:** `http://127.0.0.1:8000/api/redoc/`

---

### 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
