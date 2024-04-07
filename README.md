# Django Rest API App with Dokcer using Redis, Celery, Postgres and Firebase

## It is an e-commerce application dedicated to bookstores

# Requirments
- Docker

## Installation

To set up the application, follow these steps:

1. Clone the repository:
   git clone <repository_url>
2. Navigate to the project directory:
   cd <project_directory>
3. Run the following command :
   docker-compose up

## API Description
- Make sure nothing is running on ports 
- You can find postman collection in "Bookstore.postman_collection.json"


| Action                                                                   | HTTP Verb | Path                                                                        | Parameters  | Body                                                                       | Response                                                |
|--------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------|---------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------|
| Registration | Post| /user/register/ |  | {"username","password1","password2"} | {"access","refresh","user":{"pk","email"}} |
| Login | Post| /user/login/ |  | {"username","password""} | {"access","refresh"} |
| Create a new category | POST | /shop/categories/ |  | {"name"} | {"id","name"} | 
| Create a new product(s) | POST | /shop/products/ | | [{"name","category","price"}] | [{"id","name","category","price","total_quantity_ordered"}] | 
| Get a product | GET | /shop/products/<int:pk>/ | "product_id" | | {"id","name","category","price","total_quantity_ordered"} | 
| Get a list of products | GET | /shop/products/ | | | [{"id","name","category","price","total_quantity_ordered"}] | 
| Add items to user's cart | POST | /shop/cart/items/ | | {"product"} | {"id","quantity","product","cart"}| 
| Create an order | POST | /shop/orders/ | | {"address","city"} | {"id","status","created","updated","address","city","user"} | 
| List orders | GET | /shop/orders/ | | | [{"id","status","created","updated","address","city","user"}] | 
