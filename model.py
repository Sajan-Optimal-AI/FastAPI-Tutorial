from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel



class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    

class User(BaseModel):
    id : Optional[UUID] = uuid4()   # To generate uuid as string
    first_name : str
    last_name : str
    middle_name : Optional[str] 
    gender : Gender
    role : List[Role]
    
class UserUpdateRequest(BaseModel):
    first_name : Optional[str] 
    last_name : Optional[str]
    middle_name : Optional[str]
    role : Optional[List[Role]]