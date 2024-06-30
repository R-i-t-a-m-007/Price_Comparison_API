# Price_Comparison_API
# Price Comparison API

## Overview

This project is a basic Price Comparison API built with FastAPI, SQLAlchemy, and Pydantic. It provides endpoints for managing and retrieving product information from various retailers.

## Features

- **Retrieve Products**: Fetches a list of products, with optional filtering by name.
- **Add a Product**: Adds a new product to the database.
- **Root Endpoint**: Provides a welcome message.

## Project Structure

price-comparison-api/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
├── data/
│ └── mock_data.json
├── venv/
├── README.md


## Getting Started

### Prerequisites

- Python 3.6+
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/price-comparison-api.git
    cd price-comparison-api
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```sh
    uvicorn app.main:app --reload
    ```

5. **Access the API**:

    - Open your browser or API client (e.g., Postman) and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) for the root endpoint.
    - Use endpoints like `/api/products` to retrieve or add products.

### API Endpoints

#### Get Products

- **Endpoint**: `GET /api/products`
- **Functionality**: Retrieves a list of products. If a `name` query parameter is provided, it filters the products by the given name.
- **Example Request**: `GET /api/products?name=ProductA`
- **Example Response**:
    ```json
    [
        {
            "id": 1,
            "name": "Product A",
            "price": 100.0,
            "retailer_name": "store1"
        },
        {
            "id": 2,
            "name": "Product B",
            "price": 150.0,
            "retailer_name": "store1"
        }
    ]
    ```

#### Add a Product

- **Endpoint**: `POST /api/products`
- **Functionality**: Adds a new product to the database.
- **Example Request**:
    ```json
    {
        "name": "Product C",
        "price": 200.0,
        "retailer_name": "store2"
    }
    ```
- **Example Response**:
    ```json
    {
        "id": 3,
        "name": "Product C",
        "price": 200.0,
        "retailer_name": "store2"
    }
    ```

## Mock Data

The project includes a `data/mock_data.json` file to populate the database with initial data:

```json
{
    "store1": [
        {
            "name": "Product A",
            "price": 100.0
        },
        {
            "name": "Product B",
            "price": 150.0
        }
    ],
    "store2": [
        {
            "name": "Product C",
            "price": 200.0
        },
        {
            "name": "Product D",
            "price": 250.0
        }
    ]
}
