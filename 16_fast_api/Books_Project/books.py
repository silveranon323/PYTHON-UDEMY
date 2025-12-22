from fastapi import FastAPI , Body
app=FastAPI()

BOOKS = [
    {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'category': 'science'},
    {'title': 'The Selfish Gene', 'author': 'Richard Dawkins', 'category': 'science'},
    {'title': 'Sapiens: A Brief History of Humankind', 'author': 'Yuval Noah Harari', 'category': 'history'},
    {'title': 'Guns, Germs, and Steel', 'author': 'Jared Diamond', 'category': 'history'},
    {'title': "A Mathematician's Apology", 'author': 'G. H. Hardy', 'category': 'math'},
    {'title': 'Gödel, Escher, Bach', 'author': 'Douglas Hofstadter', 'category': 'math'}
]

@app.get("/")
async def greet():
    return {"message":"Hello World!"}
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get("author").casefold()==book_author.casefold() and book.get('category')==category.casefold():
            books_to_return.append(book)

@app.post("/book/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_books")
async def update_books(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==update_book.get("title").casefold():
            BOOKS[i]=update_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold==book_title.casefold:
            BOOKS.pop(i)