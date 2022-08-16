import time
import jwt


JWT_secret="riteshiscool"
JWT_algorithm="HS256"

#returns token generated
def tokenResponse(token : str):
    return{
        "access-token":token
    }
#signature
def tokenSign(userID : str):
    payload={
            "userID": userID,
            "expiry": time.time()+600
    }    
    token=jwt.encode(payload,JWT_secret,algorithm=JWT_algorithm)
    return(tokenResponse(token))
#decode jwt 
def decodeToken(token : str):
    decode_token=jwt.decode(token,JWT_secret,algorithm=JWT_algorithm)
    return decode_token if decode_token['expiry']>= time.time() else None
