# Library and Book Store Inventory System 📚

## Overview

The **Library and Book Store Inventory System** is a web application designed to manage the tracking, cataloging, and circulation of books in a library or bookstore. It includes inventory control, lending (borrowing and purchasing), and sales management features. This system is built using **Django** for the backend and **Django Rest Framework** for the API. The tool uses **UUIDs** as the primary key for unique identification of resources such as books, transactions, and customers.

### Features:

- **Book Cataloging**: Allows for easy tracking of books in the library or bookstore.
- **Inventory Management**: Keeps track of available, borrowed, and purchased books.
- **Lending System**: Enables users to borrow and return books with due dates and late fees.
- **Purchase and Sales Management**: Manages book purchases and sales, updating inventory accordingly.
- **Late Fee Calculation**: Automatically calculates late fees for overdue books.

## Demo


https://github.com/user-attachments/assets/7be1594e-e9cd-468b-b111-3abd8dd03f6a



## Prerequisites

- Python (v3.11 or higher)
- pip

## How to Build, Install, and Run

1. **Clone the repository**:

```bash
git clone https://github.com/Obcodelab/library-book-store-inventory.git
cd library-book-store-inventory
```

2. **Create a virtual environment**

```bash
python -m venv venv # For Windows
venv\Scripts\activate
```

```bash
python3 -m venv venv # For Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

```bash
cp .env.example .env
# Set debug to True and set secret key
```

5. **Set up the database**

```bash
python manage.py migrate
```

6. **Run the server**

```bash
python manage.py runserver
```

Once the server is running, you can access the API at http://127.0.0.1:8000/

## Contact

Discord Handle: obcodelab

X (Twitter) Handle: OBCodeLab
