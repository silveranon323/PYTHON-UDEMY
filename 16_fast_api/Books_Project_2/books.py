from typing import Optional
from fastapi import FastAPI , Body ,Path , Query , HTTPException
from pydantic import BaseModel,Field
from starlette import status
app=FastAPI()

class Books:
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date: int
    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date
        
class BookRequest(BaseModel):
    id:Optional[int]=Field(description="Id is not needed on create",default=None)
    title:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1,max_length=100)
    rating:int = Field(gt=0 , lt=6)
    published_date: int = Field(gt=1999 , lt=2031)
    model_config={
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"Coding with roby",
                "description":"a new description of book",
                "rating":5,
                "published_date":2029                }
                }
                }
BOOKS=[
    Books(1,"Title1","Author1","Desc1",4,2021),
    Books(2,"Title2","Author2","Desc2",3,2022),
    Books(3,"Title3","Author3","Desc3",2,2024),
    Books(4,"Title4","Author4","Desc4",1,2024)
]

@app.get("/books",status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404,detail="Item not found")
@app.get("/books/")
async def read_book_by_rating(book_rating:int = Query(gt=0 , lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/publish/")
async def read_books_by_publish_date(published_date: int = Query(gt=1999 , lt=2031)):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date==published_date:
            books_to_return.append(book)
    
    return books_to_return


@app.post("/books/create_book",status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    new_book=Books(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Books):
  book.id=1 if len(BOOKS)==0 else BOOKS[-1].id+1
  return book

@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_changed=False
    for i in range (len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail="Item not found")
@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int = Path(gt=0)):
    book_changed=False
    for i in range (len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            book_changed=True
            break
    if not book_changed:
        raise HTTPException(status_code=404,detail="Item not found")


