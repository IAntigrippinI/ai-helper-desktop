import json
import os

from app.config.app import app_config


class BaseConfig:
    _CONFIG_NAME = None
    _CONFIG_FILENAME = None


    def __init__(self):
        self._config_path = app_config.ROOT_PATH.joinpath("config", self._CONFIG_FILENAME)
        self._read_config()


    def _get_config_attrs(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


    def _save_config(self):
        config = {}
        for key, value in self._get_config_attrs().items():
            config[key] = value
        with open(self._config_path, "w") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)


    def _read_config(self):
        if os.path.exists(self._config_path):
            with open(self._config_path, "r") as f:
                file_config = json.load(f)
            self._fill_need_attrs(file_config)
        else:
            print(f"Fill {self._CONFIG_NAME} by default")
            self._save_config()


    def _fill_need_attrs(self, file_config: dict):
        for k, v in self._get_config_attrs().items():
            file_value = file_config.get(k)
            if not file_value:
                print(f"Setting {k} is empty")
            else:
                setattr(self, k, file_value)


