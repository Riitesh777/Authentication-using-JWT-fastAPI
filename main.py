
from fastapi import FastAPI,Depends, Form,Request

from fastapi.responses import HTMLResponse
import json
from models import userSignup,userLogin
from auth.jwt_handler import tokenSign
from auth.jwt_bearer import jwtBearer

app=FastAPI()
users=[]

@app.get("/",tags=["trail"])
def test():
    return{"hello":"world"}

@app.get("/home/{uname}",dependencies=[Depends(jwtBearer())],tags=["home"])
def home(uname):
  for user in users:  
    print(user)
    if user.username==uname :
        return{f"welcome {uname} !!"}
    else:
        return{f"{uname} not in database"}    
 

@app.post("/signup",tags=["signUp"])
def signUp(user:userSignup):
    
    users.append(user)
    
    return tokenSign(user.email)

#checking db
def check_user(data:userLogin):
    
    for user in users:
        if user.email ==  data.email and user.password == data.password:  
            return True
        return False  

@app.post("/login",tags=["login"])
def  login(user:userLogin):
    if check_user(user):
        return tokenSign(user.email)  
    else:
        return{"invalid login details"}        
