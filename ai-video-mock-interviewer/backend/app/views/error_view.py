def error_response(message:str,code:str="error",details=None):
    return {"success":False,"message":message,"error":{"code":code,"details":details}}
