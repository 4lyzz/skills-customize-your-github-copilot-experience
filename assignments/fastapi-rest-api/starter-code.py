from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "The Little Prince", "author": "Antoine de Saint-Exupery"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


class BookCreate(BaseModel):
    title: str
    author: str


@app.get("/books")
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the book, or raise an HTTP 404 error.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Assign a unique ID, add the book to the catalog, and return it.
    pass
