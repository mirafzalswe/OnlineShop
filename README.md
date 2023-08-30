# OnlineShop
# Online Shop API Documentation

Welcome to the documentation for the Online Shop API! This API is built using Django Rest Framework (DRF) and allows you to manage an online shop. You can perform various operations, including authentication, adding, updating, and deleting items, through this API.
You cannot add  or update without without registering
## Getting Started

Follow these steps to start using the Online Shop API:

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/mirafzal114/OnlineShop
   cd OnlineShop
2. **Apply Migrations:**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
3. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
4. **Run the Server:**:
   ```bash
   python manage.py runserver
Usage
Once the server is running and you have created a superuser, you can access the API through the browser or tools like Postman. The API provides endpoints for authentication and managing shop items.

# Authentication
To access most of the API features, you need to be authenticated. Use the superuser credentials to log in.

# Endpoints
`api/product/`: You can check list prodcut and add new product 
`api/product/<int:int>/`: You can update or delete product with item product
`api/categories/`: You can add new categoreis for products
`api/categories/<int:int>`: Also you can update or delete categories
   


