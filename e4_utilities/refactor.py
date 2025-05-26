import os
import glob

def get_file_paths(directory: str, extensions: list[str] = None, recursive: bool = False) -> list[str]:
    file_paths = []
    all_file_paths = glob.glob(os.path.join(directory, '*.*')) if recursive is False else glob.glob(os.path.join(directory, '**', '*.*'), recursive=True)
    for file_path in all_file_paths:
        for extension in extensions:
            if file_path.endswith(extension):
                file_paths.append(file_path)
                break

    return file_paths

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

def replace_filename(file_path: str, old_name: str, new_name: str):
    if not os.path.isfile(file_path) or not os.path.exists(file_path) or not old_name:
        return

    dirname = os.path.dirname(file_path)
    basename = os.path.basename(file_path)

    if old_name in basename:
        os.rename(file_path, os.path.join(dirname, basename.replace(old_name, new_name)))

def replace_filenames(file_paths: list[str], old_name: str, new_name: str):
    for file_path in file_paths:
        replace_filename(file_path, old_name, new_name)