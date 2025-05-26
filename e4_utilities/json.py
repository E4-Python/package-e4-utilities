import json

def load_json(file_path: str) -> dict:
    return json.load(open(file_path, 'r', encoding='utf-8'))

def save_json(file_path: str, data: dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)