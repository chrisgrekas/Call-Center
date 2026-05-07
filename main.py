from services import get_all_calls,get_call_by_id,archive_call,unarchive_call,add_note_to_call

# Uncomment to test every case
print(get_all_calls())
print(get_call_by_id("4"))
print(get_call_by_id("999"))
print(archive_call("7"))
print(archive_call("999"))
print(unarchive_call("7")) 
print(add_note_to_call("4", "Test note content"))