from dynaconf import Dynaconf

# Define settings object, pointing to a JSON file
settings = Dynaconf(
    environments=True,
    envvar_prefix="DYNACONF",
    settings_files=["config.json"]  # This is the configuration file
)

# Save the configuration values
def save_config():
    settings.set("KYB_API_URL", "http://example.com/kyc")
    settings.set("AML_API_URL", "http://example.com/aml")
    settings.set("ACH_API_URL", "http://example.com/ach")
    settings.set("BLOCKCHAIN_API_URL", "http://example.com/quorum")

    # Write changes to the JSON file
    settings.store.write("config.json")

# Read and display configuration values
def read_config():
    print("KYB_API_URL:", settings.KYB_API_URL)
    print("AML_API_URL:", settings.AML_API_URL)
    print("ACH_API_URL:", settings.ACH_API_URL)
    print("BLOCKCHAIN_API_URL:", settings.BLOCKCHAIN_API_URL)

if __name__ == "__main__":
    # Save configuration to file
    save_config()
    print("Configuration saved successfully.")

    # Read configuration from file
    print("Reading configuration:")
    read_config()
