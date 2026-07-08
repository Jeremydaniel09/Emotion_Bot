from fastapi import FastAPI,Request
from pydantic import BaseModel, Field

app = FastAPI()
class default(BaseModel):
    defaultchat: str = Field(..., description="The default message of the bot")

class basis(BaseModel):
    message: str =  Field(..., description="Laman ng message")
    responder: str = Field(..., description="If user or bot")

class response(basis):
    pass

history = [response(message= "defaultmessage", responder= "bot")]



@app.get("/")
def homelogin(answer: bool):
    if(answer):
        return {"response": True}
    else:
        return {"response": False}
    
@app.get("/botchat",response_model=response)
async def botdefault(realpepolresponse: response):
    history.append(response(message= realpepolresponse.message, responder= "user"))
    botresponse=""
    history.append(response(message = botresponse, responder="bot"))
    return history

