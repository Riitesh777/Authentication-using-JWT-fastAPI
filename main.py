
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














"""
@app.get("/items/{user}", response_class=HTMLResponse)
async def read_items(user : str):
    return ""
    <html>
        <head>
            <title>Home page</title>
        </head>
        <body>
            <h1>Welcome !!! </h1>
        </body>
    </html>
    "" 
class person(BaseModel):
    username: str
    password: str

@app.post('/postUser')
def userAdd(request:person):    
    file=open("db.json","r+")
    k=json.load(file)
    k["information"].update({request.username:request})
    # print(k["information"].get("ritesh"))
    #print(type(k))
    file.seek(0)
    d=json.dumps(k,default=vars,sort_keys=False,indent=4)
    file.write(d)
    
    file.close()
    return{0}

from fastapi.templating import Jinja2Templates
TEMPLATES = Jinja2Templates(directory=str(r"C:/Users/sonal/OneDrive/Desktop/InternProj/loginAuthentication/templates" ))
@app.get('/trail')
def trail(request:Request):
    return TEMPLATES.TemplateResponse("index.html",{"request":request})
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}    
"""