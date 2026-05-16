from services.services import get_all_calls, get_call_by_id, archive_call, unarchive_call, add_note_to_call, filter_calls, create_call, call_to_dict
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app=FastAPI()
@app.get("/")
def index():
    return {"message": "Call Center. Please go to http://127.0.0.1:8000/docs to see the swagger"}
@app.get("/health")
def health():
    return {"message": "The server is online"}
@app.get("/calls")
def get_calls(call_type: str = None, direction: str = None, is_archived: bool = None):
    if call_type == None and direction==None and is_archived==None:
        return {"calls" :get_all_calls()}
    else:
        try:
            return {"calls": [call_to_dict(call) for call in filter_calls(call_type, direction, is_archived)]}
        except ValueError as e:
            raise HTTPException(status_code=404 , detail= "Something went wrong")
        except TypeError as e:
            raise HTTPException(status_code=404 , detail= "Something went wrong")
@app.get("/calls/{call_id}")
def get_call_by_the_id(call_id:str):
    try:
        return call_to_dict(get_call_by_id(call_id))
    except ValueError as e:
        raise HTTPException(status_code= 404, detail="Call not found")
@app.patch("/calls/{call_id}/archive")
def archive_call_by_id(call_id:str):
    try:
        return call_to_dict(archive_call(call_id))
    except ValueError as e:
        raise HTTPException(status_code= 404 , detail="Something went wrong")

@app.patch("/calls/{call_id}/unarchive")
def unarchive_call_by_id(call_id:str):
    try:
        return call_to_dict(unarchive_call(call_id))
    except ValueError as e:
        raise HTTPException(status_code= 404 , detail="Something went wrong")
class NoteRequest(BaseModel):
    content: str
@app.post("/calls/{call_id}/notes")
def add_node(call_id: str , note : NoteRequest):
    try:
        return call_to_dict(add_note_to_call(call_id,note.content))
    except ValueError as e:
        raise HTTPException(status_code= 404 , detail="Something went wrong")

class CreateCallBody(BaseModel):
    direction: str
    from_: str
    to_: str
    call_type: str
    duration: int
    is_archived: bool
@app.post("/calls/create_call")
def createCall(body : CreateCallBody):
    try:
        return call_to_dict(create_call(body.direction , body.from_, body.to_ , body.call_type , body.duration , body.is_archived))
    except ValueError as e:
        raise HTTPException(status_code=404 , detail="Something went wrong")




# print(get_all_calls())
# try:
#     print(get_call_by_id("999"))
# except ValueError as e:
#     print(f"Error: {e}")
# print(add_note_to_call("4", "Test note content"))
# print(filter_calls(call_type="missed"))
# print(filter_calls(direction="inbound"))
# print(filter_calls(call_type="answered", direction="outbound"))
# try:
#     print(filter_calls(direction="wrong"))
# except ValueError as e:
#     print(f"Error: {e}")
# try:
#     print(archive_call(call_id="999"))
# except ValueError as e:
#     print(f"Error  : {e}")
# try:
#     print(filter_calls(is_archived=True))
# except TypeError as e:
#     print(f"Error: {e}")

# print(unarchive_call("3"))

# try:
#     print(unarchive_call("999"))
# except ValueError as e:
#     print(f"Error: {e}")

# print(get_call_by_id("4"))

# try:
#     print(add_note_to_call("999", "Test note"))
# except ValueError as e:
#     print(f"Error: {e}")

# try:
#     print(filter_calls(is_archived=1))
# except TypeError as e:
#     print(f"Error: {e}")

# try:
#     print(create_call("inbound", "2101010101", "6900000000", "answered", 10, False))
# except ValueError as e:
#     print(f"Error: {e}")
# try:
#     print(create_call("inbound", "210", "690", "answered", 10, False))
# except ValueError as e:
#     print(f"Error: {e}")
