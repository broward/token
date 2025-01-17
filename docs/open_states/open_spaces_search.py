import requests
import json

# Open States API Key
file = open('/home/gypsy/Project/keys/open_spaces_api_key.json', "r")
API_KEY = file.read().strip()
print(API_KEY)
file.close()

# Constants for API keys and endpoints
BILLS_ENDPOINT = "https://v3.openstates.org/bills/"
PEOPLE_ENDPOINT = "https://v3.openstates.org/people/"

# Headers for the API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

params = {
    "sort": "updated_desc",
    "q": "",   # Search query
    "page": 1,
    "per_page": 20,
    # "jurisdiction": jurisdiction,
    "created_since": "2025-01-01",
    "include": ["sponsorships"],
    "apikey": API_KEY,
    "session": None
}
    
# Function to get bills by keyword
def get_bills_by_keyword(keyword):
    """
    Fetch bills that match a given keyword.
    """
    
    bills = []
    page = 1

    while True:
        params["page"] = page
        params["q"] = keyword
        print(f"Fetching bills page {page} for keyword: {keyword}...")
        response = requests.get(
            BILLS_ENDPOINT,
            headers=HEADERS,
            params=params
        )
        if response.status_code != 200:
            print(f"Error fetching bills: {response.status_code} - {response.text}")
            break

        data = response.json()
        bills.extend(data.get("results", []))
        if not data.get("next"):  # Stop if there's no next page
            break
        page += 1

    return bills

# Function to search for a person by name
def get_person_by_name(person_name):
    """
    Search for a person by name.
    """
    print(f"Searching for person: {person_name}...")
    params["name"]=person_name
    params["page"]=1
    
    response = requests.get(
        PEOPLE_ENDPOINT,
        headers=HEADERS,
        #params={"name": person_name}
        params=params
    )
    if response.status_code != 200:
        print(f"Error fetching person: {response.status_code} - {response.text}")
        return None

    data = response.json()
    # Return the first matching person or None if no match is found
    return data.get("results", [None])[0]

# Function to write results to a JSONL file
def write_to_jsonl_file(filename, data):
    """
    Write data to a JSONL file.
    """
    with open(filename, "w") as file:
        for item in data:
            file.write(json.dumps(item) + "\n")
    print(f"Results written to {filename}")

# Main function to process bills by keyword and find matching people
def main():
    # Prompt user for the keyword
    keyword = "" #input("Enter the keyword to search for bills: ").strip()
    
    size = 1
    #keyword = "cryptocurrency"
    #keyword = "blockchain basics"
    keyword = "bullion depository"
    #keyword = "blockchain"
    #keyword = "stablecoin"
    #keyword = "digital platform payment"
    #keyword = "digital stablecoin blockchain bullion depository cryptocurrency"
    #keyword = "digital or token or stablecoin or blockchain or bullion or depository or cryptocurrency"
    jurisdiction = "Texas"
    # session = "2024"
    print(f"Searching for bills with keyword '{keyword}'...")

    # Fetch bills matching the keyword
    bills = get_bills_by_keyword(keyword)

    results = []
    for bill in bills:
        # Extract sponsor names from each bill
        sponsors = bill.get("sponsorships", [])
        for sponsor in sponsors:
            sponsor_name = sponsor.get("name")
            if sponsor_name:
                # Search for the sponsor in the people endpoint
                person = get_person_by_name(sponsor_name)
                if person:
                    # Add the bill and person data to the results
                    results.append({
                        "bill": bill,
                        "person": person
                    })

    # Write results to a JSONL file
    filename = f"results_{keyword}.jsonl"
    write_to_jsonl_file(filename, results)

# Run the script
if __name__ == "__main__":
    main()


