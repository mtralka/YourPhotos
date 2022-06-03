import json
from pathlib import Path

from app.core.config import settings
import requests


openapi_content = json.loads(requests.get(f"http://localhost:8000{settings.API_V1_STR}/openapi.json").text)

for path_data in openapi_content["paths"].values():
    for operation in path_data.values():
        tag = operation["tags"][0]
        operation_id = operation["operationId"]
        to_remove = f"{tag}-"
        new_operation_id = operation_id[len(to_remove) :]
        operation["operationId"] = new_operation_id

file_path = Path("../openapi.json")
file_path.write_text(json.dumps(openapi_content))
