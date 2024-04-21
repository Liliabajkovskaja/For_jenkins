import json
from os import path

from utils.constants import ROOT_PATH


class ConfigManager:

    with open(path.join(ROOT_PATH, 'config_ui_test.json')) as f:
        _data = f.read()

    _data = json.loads(_data)

    url = _data.get('BASE_URL')
    user_name = _data.get('BASE_USER')
    user_pass = _data.get('BASE_PASSWORD')
    browser = _data.get('BROWSER')


