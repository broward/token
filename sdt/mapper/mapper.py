import json
import os

class SingletonJSONLoader:
    """
    A singleton class to load and hold multiple JSON files in memory from the current directory.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonJSONLoader, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._loaded_data = {}
            self._initialized = True
            self._load_files_from_current_directory()

    def _load_files_from_current_directory(self):
        """
        Loads all JSON files in the directory where this script resides.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__)) + '/data'
        print('current_dir = ' + current_dir)
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".json"):
                print('loading ' + file_name)
                file_path = os.path.join(current_dir, file_name)
                self.load_json(file_path)

    def load_json(self, file_path):
        """
        Loads a JSON file into memory if it hasn't been loaded already.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The content of the JSON file.
        """
        if file_path not in self._loaded_data:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self._loaded_data[file_path] = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error reading JSON file '{file_path}': {e}")
                self._loaded_data[file_path] = {}

        return self._loaded_data[file_path]

    def get_loaded_files(self):
        """
        Returns a list of all loaded file paths.

        Returns:
            list: A list of file paths for all loaded JSON files.
        """
        return list(self._loaded_data.keys())

    def get_data(self, file_path):
        """
        Retrieves the data of a previously loaded JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The content of the JSON file if loaded, otherwise None.
        """
        return self._loaded_data.get(file_path, None)

# Usage example
if __name__ == "__main__":
    loader = SingletonJSONLoader()

    # Access loaded data
    for file_path in loader.get_loaded_files():
        data = loader.get_data(file_path)
        print(f"Data from {file_path}: {data}")

    # List loaded files
    print("Loaded files:", loader.get_loaded_files())

