from sdt.mapper.mapper import SingletonJSONLoader

# Usage example
if __name__ == "__main__":
    loader = SingletonJSONLoader()

    # Access loaded data
    for file_path in loader.get_loaded_files():
        data = loader.get_data("ach_keymap.json")
        print(f"Data from {file_path}: {data}")

    # List loaded files
    print("Loaded files:", str(loader.get_loaded_files().count))

