def validate_call_types(call_types):
    if (call_types == "answered") or (call_types == "missed") or (call_types == "voicemail"):
        return call_types
    else:
        raise ValueError(f"Invalid: {call_types}. Please enter a valid type of call. (answered, missed, voicemail)")

def validate_direction(direction):
    if (direction == "inbound") or (direction == "outbound"):
        return direction
    else:
        raise ValueError(f"Invalid: {direction}. Please enter a valid direction. (inbound, outbound)")

def validate_call_id(call_id, calls):
    for call in calls:
        if call.id == call_id:
            return call_id
    raise ValueError(f"Invalid call id. This call id does not exist.")

def validate_is_archived(is_archived):
    if isinstance(is_archived, bool):
        return is_archived
    else:
        raise TypeError(f"Invalid choice. The variable is_archived can only be True or False.")

def validate_phone_number(phone_number):
    cleaned_phone_number = phone_number.replace('+', '').replace(" ", "")
    if len(cleaned_phone_number) >= 7 and len(cleaned_phone_number) <= 15 and cleaned_phone_number.isdigit():
        return phone_number
    else:
        raise ValueError(f"The phone number has to be between 7 and 15 digits.")

def validate_duration(duration):
    if duration>=0 :
        return duration
    else:
        raise ValueError(f"Invalid duration.Please enter a valid duration")