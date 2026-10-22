# 📘 Assignment: Testing FastAPI Endpoints

## 🎯 Objective

Write automated tests for a small FastAPI book catalog using `pytest` and FastAPI's `TestClient`. Verify successful responses, returned JSON data, and a not-found error without starting a web server.

## 📝 Tasks

### 🛠️ Set Up the Test Client

#### Description
Install the testing dependencies and create a test client for the provided book catalog API.

#### Requirements
Completed program should:

- Install the required packages with `python -m pip install fastapi pytest httpx`.
- Create a `test_app.py` file and import `app` from `app.py`.
- Create a `TestClient` for the app.
- Write a test for `GET /books` that checks for HTTP status code `200`.

### 🛠️ Check the Response Data

#### Description
Test that the list endpoint returns the expected JSON book data.

#### Requirements
Completed program should:

- Send a test request to `GET /books`.
- Check that the response body is a JSON list.
- Check that the returned list contains the sample book with ID `1` and title `The Little Prince`.

### 🛠️ Test a Missing Book

#### Description
Check that the API reports a not-found response when a requested book ID does not exist.

#### Requirements
Completed program should:

- Send a test request to `GET /books/999`.
- Check that the response has HTTP status code `404`.
- Check that the JSON error detail is `Book not found`.
- Run all tests with `pytest -q` and confirm they pass.
