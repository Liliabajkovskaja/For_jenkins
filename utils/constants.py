import os
from os import path

ROOT_PATH = path.dirname(path.dirname(path.abspath(__file__)))


def default_product_id() -> int:

    data = {
        'dev': 1,
        'stage': 10,
        'prod': 30
    }
    return data[os.getenv('executed_enviroment', 'dev')]