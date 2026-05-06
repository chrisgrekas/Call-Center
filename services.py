from repo import dict_to_call,read_data_from_json

def get_all_calls():
    data=read_data_from_json()
    calls=dict_to_call(data)
    non_archived_calls=[]
    for call in calls:
        if call.is_archived==False:
            non_archived_calls.append(call)
    return non_archived_calls

print(get_all_calls())