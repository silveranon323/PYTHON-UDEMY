#pydantic examples

from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool

user=User(id=1,name="Silver Anon",is_active=True)
user2=User(id="2",name="Silver Anon",is_active=True)
print(type(user2.id))