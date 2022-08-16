from xmlrpc.client import Boolean
from fastapi import HTTPException,Request
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer,OAuth2PasswordBearer
from .jwt_handler import decodeToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class jwtBearer(HTTPBearer):
    def __init__(self,auto_Error : bool=True):
        super(jwtBearer,self).__init__(auto_error=auto_Error)

    async def  __call__(self,request:Request):
        credentials:HTTPAuthorizationCredentials = await super(jwtBearer,self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403,details="Invalid or expired token")
            return credentials.credentials    
        else:
                raise HTTPException(status_code=403,details="Invalid or expired token")

    def verifyJwt(self,jwtoken :str):
        isTokenValid: bool = False
        payload = decodeToken(jwtoken) 
        if payload:
            isTokenValid=True   
        return isTokenValid