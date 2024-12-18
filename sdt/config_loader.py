from dynaconf import Dynaconf
from threading import Lock

class ConfigLoader:
    """
    Singleton class to load configuration from env.json using DynaConf.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls, environment="test"):
        """
        Create a single instance of ConfigLoader.
        :param environment: The environment to load ('test' or 'prod')
        """
        with cls._lock:
            if cls._instance is None:
                # Initialize Dynaconf settings with env.json
                cls._instance = super(ConfigLoader, cls).__new__(cls)
                print('loaded the file')
                cls._instance.settings = Dynaconf(
                    environments=True,
                    envvar_prefix="DYNACONF",
                    settings_files=["env.json"],
                    environment=environment  # "test" or "prod"
                )
                pprint(cls._instance.settings)
            return cls._instance

    def get(self, key):
        print('getting a key:' + key)
        """
        Retrieve a configuration value.
        :param key: Key to retrieve from settings
        """
        return self.settings.get(key)

# Example usage
if __name__ == "__main__":
    # Load 'test' environment
    config = ConfigLoader(environment="")
    print("DEBUG:", config.get("DEBUG"))
    print("DATABASE_URL:", config.get("DATABASE_URL"))
    print("API_KEY:", config.get("API_KEY"))

    # Load 'prod' environment
    config_prod = ConfigLoader(environment="prod")
    print("\n[PROD ENVIRONMENT]")
    print("DEBUG:", config_prod.get("DEBUG"))
    print("DATABASE_URL:", config_prod.get("DATABASE_URL"))
    print("API_KEY:", config_prod.get("API_KEY"))


