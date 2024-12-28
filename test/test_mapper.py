from sdt.mapper.mapper import SingletonJSONLoader

# Usage example
if __name__ == "__main__":
    loader = SingletonJSONLoader()
    print("loader done")

    # Access loaded data
    for file_path in loader.get_loaded_files():
        data = loader.get_data("kyc_keymap.json")
        print(f"Data from {file_path}: {data}")


