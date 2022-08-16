from pydantic import BaseModel,EmailStr,Field


class userSignup(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    
class userLogin(BaseModel):
   
    email: EmailStr=Field(default=None)
    password: str=Field(default=None)   
    
