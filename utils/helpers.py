import os


def ensure_directory(path: str):

    if not os.path.exists(path):

        os.makedirs(path)


def clean_text(text: str):

    return text.strip()