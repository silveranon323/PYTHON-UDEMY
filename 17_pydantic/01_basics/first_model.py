from pydantic import BaseModel
class User(BaseModel):
    id:int
    name:str
    is_active:bool
input_data={
    "id":1,
    "name":"Hem",
    "is_active":True
    
}

user=User(**input_data) # here ** is used to unpack the dictionary basically all the data object will mapped to class.
print(user)