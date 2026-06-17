from pathlib import Path


class AppConfig:


    def __init__(self):

        self.ROOT_PATH = None

        self._fill_config()

    def _fill_config(self):
        self.ROOT_PATH = Path(__file__).resolve().parents[2]
        print(self.ROOT_PATH)



app_config = AppConfig()
