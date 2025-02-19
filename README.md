
# FastAPI Kafka E-Commerce

Welcome to the FastAPI Kafka E-Commerce project! This application is designed to be a scalable and efficient e-commerce platform, utilizing FastAPI for the backend, Kafka for event streaming, PostgreSQL for the database, and Redis for caching. The project also includes essential features like product management, category management, and order processing.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mehmetgencv/fastapi-kafka-ecommerce.git
   cd fastapi-kafka-ecommerce
   ```

2. **Set Up the Environment**

   Create a `.env` file in the root directory and populate it with your environment variables:

   ```bash
   DATABASE_URL=your_database_url
   KAFKA_BROKER=your_kafka_broker_url
   REDIS_URL=your_redis_url
   ```

3. **Docker Setup**

   Make sure Docker is installed on your system. You can use the following command to clean up and start the containers:

   ```bash
   docker-compose down -v
   docker-compose up --build
   ```

4. **Run Database Migrations**

   Use Alembic to handle database migrations:

   ```bash
   alembic upgrade head
   ```

## Features

### Product Management

- **CRUD Operations**: Create, read, update, and delete products.
- **Category Association**: Associate products with categories.

### Category Management

- **CRUD Operations**: Manage categories, including adding, updating, and deleting categories.
- **Product Association**: Link categories with products.

### Order Management

- **CRUD Operations**: Create, read, update, and delete orders.
- **Order Items**: Manage items within an order.
- **Order Status Tracking**: Track the status of an order.

## Usage

1. **Run the Application**

   Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API Documentation**

   Visit `http://localhost:8000/docs` for the interactive API documentation powered by Swagger UI.

## Architecture

The application follows a modular architecture with distinct layers:

- **Models**: SQLAlchemy models defining the database schema.
- **Schemas**: Pydantic models used for data validation and serialization.
- **CRUD Operations**: Functions that interact with the database.
- **Services**: Business logic handling the application's core functionalities.
- **Exception Handling**: Custom exceptions for error handling.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


