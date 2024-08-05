import os


def get_models_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))