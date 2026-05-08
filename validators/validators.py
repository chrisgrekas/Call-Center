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
def validate_call_id(call_id,calls):
    for call in calls:
        if call.id==call_id:
            return call_id
    raise ValueError(f"Invalid call id.This Call id does not exist.")
def validate_is_archived(is_archived):
    if isinstance(is_archived,bool):
        return is_archived
    else:
        raise TypeError(f"Invalid choice.The variable is_archived can only be true or false.")
def validate_phone_number(phone_number):
    if len(phone_number)==10 and (phone_number.isdigit()) :
        return phone_number
    else:
        raise ValueError(f"The phone number has to be 10 digits.")