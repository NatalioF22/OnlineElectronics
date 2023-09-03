# OnlineElectronics

---

# BuyElectronics.cloud 🛒

[![Django Version](https://img.shields.io/badge/Django-3.x-green)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

## Table of Contents 📖

- [Overview](#overview-)
- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
- [Database Models](#database-models-)
- [Contributing](#contributing-)
- [License](#license-)

## Overview 🌐

BuyElectronics.cloud is a Django-based web application designed to provide a seamless shopping experience for electronics enthusiasts. Users can create profiles, list products, and post their favorite gadgets with ease.

## Features 🌟

- **User Authentication:** Secure login and signup functionalities.
- **Profile Management:** Users can update personal information and social media links.
- **Product Listings:** Users can create, update, and delete electronic product listings.
- **Social Interactions:** Users can post about their favorite products.

## Installation 🛠️

### Prerequisites

- Python 3.x
- Django 3.x

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/NatalioF22/onlinelectronics.git
    ```

2. **Navigate to Directory**

    ```bash
    cd onlinelectronics
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Migrate Database**

    ```bash
    python manage.py migrate
    ```

5. **Run Development Server**

    ```bash
    python manage.py runserver
    ```

## Usage 🚀

After starting the development server, navigate to `http://localhost:8000/` to access the application.

## Database Models 🗄️

### Product

- `owner`: Foreign key to User
- `name`: Product name
- `product_description`: Product description
- `product_price`: Product price
- `product_link`: External link to product
- `image`: Image of the product
- `created_at`: Time of product listing creation

### Profile

- `user`: One-to-One field with User
- `first_name`: First name of user
- `last_name`: Last name of user
- `profile_image`: User's profile image
- `profile_bio`: User's biography
- `website_link`: User's website
- `facebook_link`: User's Facebook
- `instagram_link`: User's Instagram
- `linkedIn_link`: User's LinkedIn

### ProductPost

- `user`: Foreign key to User
- `product_name`: Name of the product
- `product_description`: Description of the product
- `created_at`: Time of post creation
- `product_link`: External link to the product
- `product_price`: Price of the product

## Contributing 🤝

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License 📜

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---



I hope this README serves you well! Feel free to customize it according to your specific requirements.
