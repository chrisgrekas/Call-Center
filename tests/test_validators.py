import pytest
from validators.validators import validate_call_types, validate_direction, validate_call_id, validate_is_archived, validate_phone_number , validate_duration
from models.models import Call
def test_validate_call_types():
    assert validate_call_types(call_types="answered") == "answered"
    assert validate_call_types(call_types="missed") == "missed"
    assert validate_call_types(call_types="voicemail") == "voicemail"
    with pytest.raises(ValueError, match=f"Invalid: test ςρονγ"):
        validate_call_types(call_types="test")

def test_validate_direction():
    assert validate_direction(direction="inbound") == "inbound"
    assert validate_direction(direction="outbound") == "outbound"
    with pytest.raises(ValueError, match="Invalid: wrong direction"):
        validate_direction(direction="wrong direction")

def test_validate_call_id():
    mock_calls = [
        Call("1007d973-e3e7-47de-9d0c-cea33048acc1", "inbound", "+33 6 12 34 56 78", "+33 1 23 45 67 89", "answered", 120, False, "2025-04-10T14:32:00Z")
    ]
    assert validate_call_id(call_id="1007d973-e3e7-47de-9d0c-cea33048acc1",calls=mock_calls) =="1007d973-e3e7-47de-9d0c-cea33048acc1"
    with pytest.raises(ValueError, match="Invalid call id. This call id does not exist."):
        validate_call_id(call_id="wrongid",calls=mock_calls)

def test_validate_is_archived():
    assert validate_is_archived(is_archived=True) == True
    assert validate_is_archived(is_archived=False) == False
    with pytest.raises(TypeError, match="Invalid choice."):
        validate_is_archived(is_archived="wrong boolean")

def test_validate_phone_number():
    assert validate_phone_number(phone_number="30 276 10 23 0 48") == "30 276 10 23 0 48"
    with pytest.raises(ValueError,match="The phone number has to be between 7 and 15 digits."):
        validate_phone_number(phone_number="1234")

def test_validate_duration():
    assert validate_duration(duration=5) ==5
    with pytest.raises(ValueError,match="Invalid duration.Please enter a valid duration"):
        validate_duration(-1)
