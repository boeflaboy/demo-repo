from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/books')
async def list_all_books():
    return BOOKS

@app.get('/books/get_book_by_author/{book_author}')
async def get_book_by_author(author: str):
    books_from_author = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_from_author.append(book)
    return books_from_author


#this is a path paramater
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        else:
            return {"message": "book not found"}

# This is a query paramater
@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# this is a path and query parameter
@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            book_to_return.append(book)

    return book_to_return


@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "The new book has been succesfully added to the collection"}

@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_to_delete: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_to_delete.casefold():
            BOOKS.pop(i)
            break
    return {'message': "selected book has been deleted"}




