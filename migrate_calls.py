import json
import uuid
import os
from datetime import datetime, timezone
from repositories.repo import read_data_from_json

calls = read_data_from_json()

clean_calls = []
for call in calls:
    if call['id'] in [str(i) for i in range(1, 16)]:
        clean_calls.append(call)

for call in clean_calls:
    call['id'] = str(uuid.uuid4())
    call['created_at'] = datetime.now(timezone.utc).isoformat()

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data', 'calls.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(clean_calls, f, indent=4, ensure_ascii=False)

print("Done!")