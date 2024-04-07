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
|--------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------|---------------------------------------------|--------------------------------------|---------------------------------------------------------|
| Create a new category | POST |  |  | | | 
| Create a new product | POST | /shop/products/ | | [{"name","category","price"}] | | 
| Get a product | GET | /shop/products/<int:pk>/ | "product_id" | | | 
| Get a list of products | GET | /shop/products/ | | | | 
| Add items to user's cart | POST | /shop/cart/items/ | | {"product"} | | 
| Create an order | POST | /shop/orders/ | | | | 
| List orders | GET | /shop/orders/ | | | | 
