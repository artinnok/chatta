import os

import trafaret
from trafaret_config import read_and_validate


TRAFARET = trafaret.Dict({
    trafaret.Key('host'): trafaret.IP,
    trafaret.Key('port'): trafaret.Int(),
})


def get_config():
    BASE_PATH = os.getcwd()

    config = read_and_validate(BASE_PATH + '/config/settings.yml', TRAFARET)
    config['base_path'] = BASE_PATH

    return config
