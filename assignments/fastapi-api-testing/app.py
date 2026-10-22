from fastapi import FastAPI, HTTPException

app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "The Little Prince", "author": "Antoine de Saint-Exupery"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
