import os

def replace_text(file_path: str, old_text: str, new_text: str):
    if not os.path.exists(file_path) or not old_text:
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.replace(old_text, new_text)
            f.write(line)

def replace_texts(file_path: str, text_tuples: list[tuple[str, str]]):
    for text_tuple in text_tuples:
        replace_text(file_path, *text_tuple)