from services import get_all_calls,get_call_by_id,archive_call,unarchive_call,add_note_to_call,filter_calls

# Uncomment to test every case
# print(get_all_calls())
# print(get_call_by_id("4"))
# print(get_call_by_id("999"))
# print(archive_call("7"))
# print(archive_call("999"))
# print(unarchive_call("7")) 
# print(add_note_to_call("4", "Test note content"))
# print(filter_calls(call_type="missed"))
# print(filter_calls(direction="inbound"))
print(filter_calls(call_type="answered", direction="outbound"))
# print(filter_calls(is_archived=True))