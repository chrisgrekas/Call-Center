from services.services import get_all_calls, get_call_by_id, archive_call, unarchive_call, add_note_to_call, filter_calls, create_call, call_to_dict
from pydantic import BaseModel
from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs.txt"
)
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        logger.info(f"{request.method} {request.url.path} {response.status_code} {duration:.2f}s")
        return response
app = FastAPI()
app.add_middleware(LoggingMiddleware)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
