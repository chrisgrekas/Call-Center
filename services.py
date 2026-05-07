from repo import dict_to_call,read_data_from_json,update_data_to_json

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

# print(get_call_by_id("4"))

