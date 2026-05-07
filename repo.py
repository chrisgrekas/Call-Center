import json
import os
from models import Call

def read_data_from_json():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'calls.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
# print(read_data_from_json())
def write_data_to_json(new_call):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'calls.json')
    if os.path.exists(file_path):
        with open(file_path,'r',encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data=[]
    else:
        data=[]
    data.append(new_call)
    with open(file_path,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)


    


data=read_data_from_json()
def update_data_to_json(data,updated_call):
    upd_call=(updated_call.__dict__)
    upd_call = dict(updated_call.__dict__)
    upd_call["from"] = upd_call.pop("from_")
    upd_call["to"] = upd_call.pop("to_")
    for i, call in enumerate(data):
        if call["id"] == upd_call["id"]:
            data[i] = upd_call
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir,'calls.json')
            with open(file_path,'w',encoding='utf-8') as file:
                json.dump(data,file,indent=4,ensure_ascii=False)
            return upd_call
    return None
            



def dict_to_call(data):
    calls=[]
    for call in data:
        call_to_obj=Call(call["id"],call["direction"],call["from"],call["to"],call["call_type"],call["duration"],call["is_archived"],call["created_at"])
        calls.append(call_to_obj)
    return calls
    
# print(dict_to_call(data))
# test_data = [
#     {
#         "id": "16",
#         "direction": "inbound",
#         "from": "+33 6 12 34 56 78",
#         "call_type": "answered"
#     }
# ]

# write_data_to_json(test_data)
# print(read_data_from_json())