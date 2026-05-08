class Call:
    def __init__(self,id,direction,from_,to_,call_type,duration,is_archived,created_at,notes=None):
        self.id=id
        self.direction=direction
        self.from_=from_
        self.to_=to_
        self.call_type=call_type
        self.duration=duration
        self.is_archived=is_archived
        self.created_at=created_at
        self.notes=notes if notes is not None else []

    def __repr__(self):
        return (f"Call(id='{self.id}', direction='{self.direction}', "
                f"  type='{self.call_type}', "
                f"duration={self.duration}, archived={self.is_archived},notes={self.notes})")

class Note:
    def __init__(self,id,call_id,content):
        self.id=id
        self.call_id=call_id
        self.content=content
    def __repr__(self):
        return f"Note(id='{self.id}', call_id='{self.call_id}', content='{self.content}')"


# test_call = Call(
#     id="1",
#     direction="inbound",
#     from_="+33 6 12 34 56 78",
#     to_="+33 1 23 45 67 89",
#     call_type="answered",
#     duration=120,
#     is_archived=False,
#     created_at="2025-04-10T14:32:00Z"
# )

# print(test_call)
# # test_note = note(id="n1", call_id="3", content="Customer left a message about their invoice")
# print(test_note)

