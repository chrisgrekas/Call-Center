from services.services import get_all_calls,get_call_by_id,archive_call,unarchive_call,add_note_to_call,filter_calls

# Uncomment to test every case
# print(get_all_calls())
# try:
#     print(get_call_by_id("999"))
# except ValueError as e:
#     print(f"Error: {e}")
# print(add_note_to_call("4", "Test note content"))
# print(filter_calls(call_type="missed"))
# print(filter_calls(direction="inbound"))
# print(filter_calls(call_type="answered", direction="outbound"))
# print(filter_calls(is_archived=True))
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