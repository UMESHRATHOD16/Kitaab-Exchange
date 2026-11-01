# 📚 Kitaab Exchange API

A simple REST API built with **FastAPI** that allows students to exchange used books. Users can register, list their books for sale, browse available books, update book details, and mark books as sold.

## 🚀 Features

- **User Registration** – Register users with name, email, and college details.
- **Book Listing** – Add books with title, author, price, and owner information.
- **Browse Books** – Retrieve all available (unsold) books.
- **Search & Filter** – Filter books by title and author.
- **Update Book Details** – Update book price and selling status.
- **Mark as Sold** – Mark a listed book as sold.
- **API Key Authentication** – Protect write operations using an API key.
- **SQLite Database** – Store users and books with a one-to-many relationship.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| SQLModel | Database models and ORM |
| SQLite | Database |
| Uvicorn | ASGI server |

## 📁 Project Structure

```text
kitab-exchange/
│
├── main.py
├── database.py
├── auth.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── users.py
│   └── books.py
│
├── routes/
│   ├── __init__.py
│   ├── users.py
│   └── books.py
│
└── kitaab.db
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd kitab-exchange
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🔑 Authentication

Write operations require an API key passed through the `X-API-Key` request header.

```http
X-API-Key: my_secret_api_key
```

The current implementation uses a hardcoded demo API key in `auth.py`. For production, move it to an environment variable.

## 🔗 API Endpoints

### Users

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/users/` | Register a new user | Required |
| GET | `/users/` | Retrieve all users | Not required |

### Books

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/books/` | Add a new book | Required |
| GET | `/books/` | Retrieve available books | Not required |
| PATCH | `/books/{book_id}/` | Update book details | Required |
| PATCH | `/books/{book_id}/mark_sold/` | Mark a book as sold | Required |

### Book Filtering

The books listing endpoint supports optional query parameters:

```http
GET /books/?title=Python
GET /books/?author=James
GET /books/?title=Python&author=James
```

Only unsold books are returned by the listing endpoint.

## 📝 Example Requests

### Register a User

```json
{
  "name": "Umesh",
  "email": "umesh@example.com",
  "college": "NIT Jalandhar"
}
```

### Add a Book

```json
{
  "title": "Python Programming",
  "author": "John Smith",
  "price": 350,
  "user_id": 1
}
```

### Update Book Price

```json
{
  "price": 300
}
```

### Update Selling Status

```json
{
  "isSold": true
}
```

## 🗄️ Database Design

The application uses two main tables:

**User**
- `id` – Primary key
- `name` – User's name
- `email` – Unique email address
- `college` – College name

**Book**
- `id` – Primary key
- `title` – Book title
- `author` – Author name
- `price` – Book price
- `isSold` – Selling status
- `user_id` – Foreign key referencing the owner

**Relationship:** One user can list multiple books, while each book belongs to one user.

## 🔮 Future Improvements

- Add user login and registration authentication.
- Move API keys and secrets to environment variables.
- Implement database migrations using Alembic.
- Add pagination and sorting for book listings.
- Add book categories and descriptions.
- Implement ownership-based authorization.
- Build a frontend for a complete book exchange platform.

## 👨‍💻 Author

**Rathod Umesh**

Built as a learning project to explore REST API development, FastAPI, SQLModel, database relationships, CRUD operations, and API authentication.

---

⭐ If you find this project useful, consider giving it a star!