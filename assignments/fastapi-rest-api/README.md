# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small in-memory book catalog API with FastAPI. Practice creating REST endpoints, using path parameters, validating request data, and returning appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Create the API and List Books

#### Description
Set up the FastAPI application and implement an endpoint that returns every book in the provided catalog.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`.
- Implement `GET /books` so it returns the `books` list from the starter code as JSON.
- Run the application with `uvicorn starter_code:app --reload` and confirm the endpoint works at `/books` and the interactive API documentation loads at `/docs`.

### 🛠️ Retrieve a Book by ID

#### Description
Add an endpoint that looks up a single book using its ID from the URL path.

#### Requirements
Completed program should:

- Implement `GET /books/{book_id}` using an integer path parameter.
- Return the matching book when its ID exists.
- Raise an HTTP 404 error when no book has the requested ID.

### 🛠️ Add a New Book

#### Description
Create an endpoint that accepts book details as JSON and adds a new book to the in-memory catalog.

#### Requirements
Completed program should:

- Use the provided `BookCreate` Pydantic model to validate a request containing a title and author.
- Implement `POST /books` to assign a unique integer ID, add the book to the catalog, and return the created book.
- Return HTTP status code 201 for a successful creation.
- Let FastAPI return a validation error when required request fields are missing or invalid.
