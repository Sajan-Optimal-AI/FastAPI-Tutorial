
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from model import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db : List[User] = [
    User(
        id = UUID("0cbcd220-05dc-49d5-b1bf-d963d98d71ad"),
        first_name = "Pon",
        last_name = "Sajan" ,
        gender = Gender.male,
        role = [Role.admin]
    ),
    User(
        id = UUID("11c9b753-ab47-4fa6-9da7-3e0671ba54b1"),
        first_name ="Sathya",
        last_name = "Rajamuthu",
        gender = Gender.female,
        role = [Role.student,Role.admin]
    )
]


@app.get("/")         # get root 

async def root():
    return {"Hello":"Mundo"}                 #root value is {"Hello":"World"}

@app.get("/user")

async def fetch_user():
    return db;

@app.post("/user")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/user/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return user_id
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} doesnot exist"
    )
@app.put("/user/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.role is not None:
                user.role = user_update.role
            return
    raise HTTPException(
            status_code = 404,
            detail = f"user with id:{user_id} does not exists"
        )
