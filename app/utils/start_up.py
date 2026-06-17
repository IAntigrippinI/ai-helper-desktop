import os

from app.config.app import app_config

def _init_path():
    config_dir_name = app_config.ROOT_PATH.joinpath("config")
    if not os.path.exists(config_dir_name):
        os.makedirs(config_dir_name)
        print(f"Create config dir: {config_dir_name}")
