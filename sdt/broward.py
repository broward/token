from openai import OpenAI
import openai
import requests
import json

# Open States API Key
file = open('/home/gypsy/Project/keys/openai_api_key.json', "r")
API_KEY = file.read().strip()
print(API_KEY)
file.close()

# Define the REST endpoint and API key
FILE_URL = "https://api.openai.com/v1/files"   
UPLOAD_URL = "https://api.openai.com/v1/uploads" 

# Define headers, including the API key
upload_headers = {
    "Authorization": f"Bearer {API_KEY}",  # Replace "Bearer" if your API uses a different header format
    "Content-Type": "application/json"  # Adjust content type if needed
}

# Define headers, including the API key
file_headers = {
    "Authorization": f"Bearer {API_KEY}",  # Replace "Bearer" if your API uses a different header format
    "Content-Type": "multipart/form-data"  # Adjust content type if needed
}

# Define the request payload (if required)
data = {
    "purpose": "fine-tune",
    "file": "@schema.json"
  }

payload = json.dumps(data)

import openai

# Initialize the OpenAI client with your API key
client = openai.OpenAI(API_KEY)

# Function to upload a file
def upload_file(file_path, purpose="fine-tune"):
    """
    Upload a file to OpenAI.

    Args:
        file_path (str): Path to the file to be uploaded.
        purpose (str): The purpose of the file (e.g., 'fine-tune').

    Returns:
        dict: The response from OpenAI.
    """
    try:
        # Open the file and upload
        with open(file_path, "rb") as file:
            response = client.File.create(file=file, purpose=purpose)
        print("File uploaded successfully!")
        print(f"File ID: {response['id']}")
        return response
    except Exception as e:
        print(f"An error occurred while uploading the file: {e}")
        return None

# Main function to execute the upload
if __name__ == "__main__":
    # Provide the file path and purpose
    file_path = "schema.json"  # Replace with the path to your file
    purpose = "fine-tune"  # Adjust purpose as needed (e.g., 'answers', 'classifications')

    # Call the upload function
    upload_file(file_path, purpose)
