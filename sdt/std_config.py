# sdt_Config.py

import json

class SDTConfig:
    _instance = None
    _config_data = None

    def __new__(cls, config_file="config/env.json"):
        if cls._instance is None:
            cls._instance = super(SDTConfig, cls).__new__(cls)
            cls._instance._load_config(config_file)
        return cls._instance

    def _load_config(self, config_file):
        try:
            with open(config_file, "r") as file:
                self._config_data = json.load(file)
        except FileNotFoundError:
            self._config_data = {}
            print(f"Warning: {config_file} not found. Using empty configuration.")

    def get_value(self, key):
        """Retrieve the value for a given key from the config."""
        return self._config_data.get(key, None)
