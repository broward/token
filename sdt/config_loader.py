# config_loader.py

import json
import os
from threading import Lock

class ConfigLoader:
    """
    Singleton class to load environment-specific configuration from a JSON file.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Create a single instance of ConfigLoader.
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ConfigLoader, cls).__new__(cls)
                cls._instance._load_config()
            return cls._instance

    def _load_config(self):
        """
        Load the configuration from a JSON file based on the SDT_ENV environment variable.
        """
        env = os.getenv("env.json", "test")  # Default to "test" if SDT_ENV is not set
        if env not in ["test", "prod"]:
            raise ValueError(f"Invalid SDT_ENV value: {env}. Must be 'test' or 'prod'.")

        # Load the JSON configuration file
        try:
            with open("env.json", "r") as file:
                all_config = json.load(file)
                self.config = all_config.get(env, {})
                if not self.config:
                    raise ValueError(f"No configuration found for environment: {env}.")
        except FileNotFoundError:
            raise FileNotFoundError("The configuration file 'env.json' was not found.")
        except json.JSONDecodeError:
            raise ValueError("The configuration file 'env.json' contains invalid JSON.")

    def get(self, key):
        """
        Retrieve a configuration value for the selected environment.
        :param key: The key to retrieve from the configuration.
        """
        return self.config.get(key, None)

# Example usage
if __name__ == "__main__":
    # Ensure SDT_ENV is set in the environment
    os.environ["SDT_ENV"] = "test"  # Set this for testing purposes

    # Create the ConfigLoader instance
    config = ConfigLoader()

    # Access configuration values
    print("DEBUG:", config.get("DEBUG"))
    print("DATABASE_URL:", config.get("DATABASE_URL"))
    print("API_KEY:", config.get("API_KEY"))

