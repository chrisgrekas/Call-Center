from repositories.repo import dict_to_call, read_data_from_json, update_data_to_json, write_data_to_json
from models.models import Call, Note
from validators.validators import validate_call_types, validate_direction, validate_call_id, validate_is_archived, validate_phone_number , validate_duration
import uuid
from datetime import datetime, timezone

def get_all_calls():
    data = read_data_from_json()
    calls = dict_to_call(data)
    non_archived_calls = []
    for call in calls:
        if not call.is_archived:
            non_archived_calls.append(call_to_dict(call))
    return non_archived_calls



def archive_call(call_id):
    data = read_data_from_json()
    calls = dict_to_call(data)
    validate_call_id(call_id, calls)
    for call in calls:
        if call.id == call_id:
            call.is_archived = True
            update_data_to_json(data, call)
            return call
    return None

def get_call_by_id(call_id):
    data = read_data_from_json()
    calls = dict_to_call(data)
    validate_call_id(call_id, calls)
    for call in calls:
        if call.id == call_id:
            return call
    return None

def unarchive_call(call_id):
    data = read_data_from_json()
    calls = dict_to_call(data)
    validate_call_id(call_id, calls)
    for call in calls:
        if call_id == call.id:
            call.is_archived = False
            update_data_to_json(data, call)
            return call
    return None

def add_note_to_call(call_id, content):
    data = read_data_from_json()
    calls = dict_to_call(data)
    validate_call_id(call_id, calls)
    note_id = str(uuid.uuid4())
    new_note = Note(note_id, call_id, content)
    for call in calls:
        if call.id == call_id:
            call.notes.append(new_note)
            update_data_to_json(data, call)
            return call
    return None


def filter_calls(call_type=None, direction=None, is_archived=None):
    if call_type is not None:
        validate_call_types(call_type)
    if direction is not None:
        validate_direction(direction)
    if is_archived is not None:
        validate_is_archived(is_archived)
    data = read_data_from_json()
    calls = dict_to_call(data)
    filter_calls_list = []
    for call in calls:
        if (call_type is None or call.call_type == call_type) and (direction is None or call.direction == direction) and (is_archived is None or call.is_archived == is_archived):
            filter_calls_list.append(call)
    return filter_calls_list

def create_call(direction, from_, to_, call_type, duration, is_archived):
    call_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc).isoformat()
    validate_call_types(call_type)
    validate_direction(direction)
    validate_is_archived(is_archived)
    validate_phone_number(from_)
    validate_phone_number(to_)
    validate_duration(duration)
    new_call = Call(call_id, direction, from_, to_, call_type, duration, is_archived, created_at)
    new_call_dict = dict(new_call.__dict__)
    new_call_dict["from"] = new_call_dict.pop("from_")
    new_call_dict["to"] = new_call_dict.pop("to_")
    write_data_to_json(new_call_dict)
    return new_call

def call_to_dict(calls):
    new_call_dict = dict(calls.__dict__)
    new_call_dict["from"] = new_call_dict.pop("from_")
    new_call_dict["to"] = new_call_dict.pop("to_")
    return new_call_dict
