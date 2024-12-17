{
  "name": "name",
  "age": "age",
  "address": "address",
  "address.street": "address.street",
  "address.city": "address.city",
  "address.postalCode": "address.postalcode"
}

import json

def read_json_config(file_path):
    """
    Reads a JSON configuration file and processes keys with dot-notation into a nested dictionary.
    :param file_path: Path to the JSON configuration file.
    :return: Processed nested dictionary.
    """
    def set_nested_value(data, key, value):
        """ Helper function to set a nested value using dot-notation keys. """
        keys = key.split(".")
        d = data
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value

    # Load the JSON file
    with open(file_path, 'r') as file:
        config = json.load(file)

    nested_config = {}
    for key, value in config.items():
        set_nested_value(nested_config, key, value)

    return nested_config

def flatten_and_replace_keys(json_obj, replacements):
    """
    Flattens a JSON object and replaces keys based on a replacements mapping.
    :param json_obj: The input JSON object.
    :param replacements: A dictionary with key-value pairs for replacements.
    :return: Flattened JSON object with keys replaced.
    """
    def flatten(obj, parent_key='', sep='.'):
        """ Helper function to flatten a nested JSON object. """
        items = []
        for k, v in obj.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def replace_keys(flat_obj, replacements):
        """ Replace keys in a flattened object based on replacements mapping. """
        return {replacements.get(k, k): v for k, v in flat_obj.items()}

    # Flatten the JSON object
    flat_obj = flatten(json_obj)
    # Replace keys
    replaced_obj = replace_keys(flat_obj, replacements)

    return replaced_obj

if __name__ == "__main__":
    config_file = "config.json"  # Path to your JSON configuration file
    nested_config = read_json_config(config_file)

    replacements = {
        "name": "fullName",
        "address.street": "streetName",
        "address.city": "cityName"
    }  # Example replacements mapping

    updated_json = flatten_and_replace_keys(nested_config, replacements)

    print("Updated JSON with Replaced Keys:")
    print(json.dumps(updated_json, indent=4))

