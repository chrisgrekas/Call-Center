# Call Center

A simple call management system built in Python.

## What it does

Loads call data from a JSON file and exposes functions to manage calls:

- Get all active (non-archived) calls
- Get a single call by ID
- Create a new call
- Archive / unarchive a call
- Add notes to a call
- Filter calls by type, direction, or archived status
- Input validation with descriptive error messages

## Stack

- Python 3
- No external dependencies

## How to run

```bash
python main.py
```

## Validation

The following inputs are validated:

- `call_type` must be answered, missed, or voicemail
- `direction` must be inbound or outbound
- `is_archived` must be a boolean
- `phone_number` must be 10 digits
- `call_id` must exist in the system