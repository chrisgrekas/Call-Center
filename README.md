# Call Center

A simple call management system built in Python.

## What it does

Loads call data from a JSON file and exposes APIs to manage calls:

- Get all active (non-archived) calls
- Get a single call by ID
- Create a new call
- Archive / unarchive a call
- Add notes to a call
- Filter calls by type, direction, or archived status
- Input validation with descriptive error messages

## Stack

- Python 3
- FastAPI, Uvicorn, Pydantic

## How to run

First, install the required dependencies:

```bash
pip install fastapi uvicorn pydantic
```

Then, start the server:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

Swagger UI are available at http://127.0.0.1:8000/docs

## Endpoints

| GET | /calls | Get all non-archived calls (supports filtering) |
| GET | /calls/{call_id} | Get a single call by ID |
| POST | /calls | Create a new call |
| PATCH | /calls/{call_id}/archive | Archive a call |
| PATCH | /calls/{call_id}/unarchive | Unarchive a call |
| POST | /calls/{call_id}/notes | Add a note to a call |
| GET | /health | Health check |

## Validation

The following inputs are validated:

- `call_type` must be answered, missed, or voicemail
- `direction` must be inbound or outbound
- `is_archived` must be a boolean
- `phone_number` must be between 7 and 15 digits
- `call_id` must exist in the system
- `duration` must be a non-negative number