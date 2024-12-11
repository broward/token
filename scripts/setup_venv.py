import os
import subprocess
import sys

def create_and_activate_venv(venv_name="venv"):
    """
    Creates and activates a virtual environment and prints 'Hello World' to the terminal.
    """
    # Step 1: Check if virtual environment exists
    if not os.path.exists(venv_name):
        print(f"Creating virtual environment: {venv_name}")
        subprocess.check_call([sys.executable, "-m", "venv", venv_name])
    else:
        print(f"Virtual environment '{venv_name}' already exists.")

    # Step 2: Determine the activation script based on the OS
    activate_script = os.path.join(venv_name, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_name, "bin", "activate")

    if not os.path.exists(activate_script):
        print("Error: Activation script not found.")
        sys.exit(1)

    # Step 3: Print Hello World
    print("Activating virtual environment and printing 'Hello World'")
    if os.name == "nt":  # Windows
        subprocess.call(f"{activate_script} && echo Hello World", shell=True)
    else:  # Unix/Linux/Mac
        subprocess.call(f"source {activate_script} && echo Hello World", shell=True)


if __name__ == "__main__":
    create_and_activate_venv()

