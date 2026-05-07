def validate_call_types(call_types):
    if (call_types=="answered") or (call_types=="missed")  or (call_types=="voicemail"):
        return call_types
    else:
        raise ValueError(f"Invalid: {call_types}.Please enter a valid type of call.(answered,missed,voicemail)")
def validate_direction(direction):
    if (direction=="inbound") or (direction=="outbound"):
        return direction
    else:
        raise ValueError(f"Invalid: {direction}. Please enter a valid direction.(inbound,outbound)")
