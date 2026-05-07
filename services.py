from repo import dict_to_call,read_data_from_json,update_data_to_json
from models import Note
import uuid

def get_all_calls():
    data=read_data_from_json()
    calls=dict_to_call(data)
    non_archived_calls=[]
    for call in calls:
        if call.is_archived==False:
            non_archived_calls.append(call)
    return non_archived_calls

# print(get_all_calls())
def archive_call(call_id):
    data=read_data_from_json()
    calls=dict_to_call(data)
    for call in calls:
        if call.id==call_id:
            call.is_archived=True
            update_data_to_json(data,call)
            return call
    return None

def get_call_by_id(call_id):
    data=read_data_from_json()
    calls=dict_to_call(data)
    for call in calls:
        if call.id==call_id:
            return call
    return None

def unarchive_call(call_id):
    data=read_data_from_json()
    calls=dict_to_call(data)
    for call in calls:
        if call_id==call.id:
            call.is_archived=False
            update_data_to_json(data,call)
            return call
    return None

def add_note_to_call(call_id,content):
    data=read_data_from_json()
    calls=dict_to_call(data)
    note_id=str(uuid.uuid4())
    new_note=Note(note_id,call_id,content)
    for call in calls:
        if call.id==call_id:
            call.notes.append(new_note)
            update_data_to_json(data,call)
            return call
    return None


def filter_calls(call_type=None, direction=None, is_archived=None):
    data=read_data_from_json()
    calls=dict_to_call(data)
    filter_calls_list=[]
    for call in calls:
        if (call_type is None or call.call_type==call_type) and (direction is None or call.direction==direction) and (is_archived is None or call.is_archived==is_archived):
            filter_calls_list.append(call)
    return filter_calls_list
        
        

