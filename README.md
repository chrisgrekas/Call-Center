[![CI](https://github.com/chrisgrekas/Call-Center/actions/workflows/ci.yaml/badge.svg)](https://github.com/chrisgrekas/Call-Center/actions/workflows/ci.yaml)

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
pip install -r requirements.txt
```

Then, start the server:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

Swagger UI is available at http://127.0.0.1:8000/docs

## Live demo

https://call-center-rlc4.onrender.com

## How to run the tests

```bash
pytest tests/ -v
```

## CI/CD

This project uses GitHub Actions to run automated tests on every push and pull request to `main`.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /calls | Get all non-archived calls (supports filtering) |
| GET | /calls/{call_id} | Get a single call by ID |
| POST | /calls | Create a new call |
| PATCH | /calls/{call_id}/archive | Archive a call |
| PATCH | /calls/{call_id}/unarchive | Unarchive a call |
| POST | /calls/{call_id}/notes | Add a note to a call |
| PATCH | /calls/{call_id}/notes/{note_id} | Update a note |
| GET | /health | Health check |

## Validation

The following inputs are validated:

- `call_type` must be answered, missed, or voicemail
- `direction` must be inbound or outbound
- `is_archived` must be a boolean
- `phone_number` must be between 7 and 15 digits
- `call_id` must exist in the system
- `duration` must be a non-negative number

## Features implemented

**Core**
- List all non-archived calls with filtering by type, direction, and archived status
- Fetch a single call by ID
- Create a new call with full validation
- Archive / unarchive a call
- Add a note to a call
- Update a note on a call

**Bonus**
- Input validation with descriptive error messages
- Request logging middleware
- CI/CD with GitHub Actions
- Live deployment on Render

## Known limitations

- Data is stored in a flat JSON file — not suitable for concurrent writes or large datasets
- No authentication or authorization on any endpoint
- Notes cannot be deleted