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

