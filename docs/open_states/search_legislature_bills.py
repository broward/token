import requests
import json
import sys, os

# Open States API Key
file = open('../keys/open_spaces_api_key.json', "r")
API_KEY = file.read().strip()
print(API_KEY)
file.close()

# Base URLs for Open States API
BASE_BILLS_URL = "https://v3.openstates.org/bills/"
BASE_PEOPLE_URL = "https://v3.openstates.org/people/"
OUTPUT_FILE = "pending_legislation.txt"

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

def search_bills_by_keyword(page, keyword, jurisdiction="all", session=None):
    """
    Searches bills by title or subject for a specific keyword or phrase.

    Args:
        keyword (str): Word or phrase to search for.
        jurisdiction (str): The jurisdiction to filter by (default is "all").
        session (str): Legislative session to filter by (optional).

    Returns:
        list: List of bills with title, subject, and sponsor information.
    """
    params = {
        "sort": "updated_desc",
        "q": keyword,   # Search query
        "page": page,
        "per_page": 20,
        # "jurisdiction": jurisdiction,
        "created_since": "2024-11-01",
        "include": ["sponsorships"],
        "apikey": API_KEY,
        "session": session
    }
    
    try:
        response = requests.get(BASE_BILLS_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        bills = data.get("results", [])
        results = []
        
        for bill in bills:
            jurisdiction = bill.get("jurisdiction", [])
            title = bill.get("title", "No title available")
            identifier = bill.get("identifier", "no identifier available")
            subjects = bill.get("subject", [])
            sponsor = bill.get("sponsor", "no sponsor listed")
            sponsors = bill.get("sponsorships", [])
            updated = bill.get("updated_at", "no date available")
            
            # Collect sponsor names and IDs
            sponsor_details = [
                {"name": sponsor.get("name"), "id": sponsor.get("id"), "person": sponsor.get("person")}
                for sponsor in sponsors
            ]
            
            results.append({
                "jurisdiction": jurisdiction,
                "title": title,
                "identifier": identifier,
                "subjects": subjects,
                "sponsor": sponsor,
                "sponsors": sponsor_details,
                "updated": updated})
        
            if results:
                with open(OUTPUT_FILE, "a") as f:
                    # f.write(f"Found {len(results)} bills:")
                    for result in results:
                        f.write(f"\n\nTitle: {result['title']}")
                        f.write(f"\nJurisdiction: {result['jurisdiction']['name']} - {result['identifier']}")
                        
                        if result["sponsors"]:
                            for sponsor in result["sponsors"]:
                                f.write(f"\n{sponsor['name']}")

                                person = sponsor["person"]
                                if person:
                                    id = person["id"]

                                    #if id:
                                    #    offices = get_sponsor_details(id)

                                    #    if offices:
                                    #        for office in offices:
                                    #            print(office)
                                                #f.write(f"\n{office['address']}")
                        else:
                            f.write("\nSponsors: None")
            else:
                print(" Sponsors: None")
        else:
            print(" No bills found.")

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return []

def get_sponsor_details(sponsor_id):
    
    # Retrieves detailed information about a sponsor by their ID.

    url = f"{BASE_PEOPLE_URL}/"
    params = {"id": sponsor_id,
              "include": ["offices"],
              "apikey": API_KEY}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving sponsor details: {e}")
        return {}

def main():
    # Search for bills with a specific keyword
    keyword = "" #input("Enter a keyword or phrase to search in bill titles and subjects: ").strip()
    jurisdiction = "all" #input("Enter jurisdiction (default is 'all'): ").strip() or "all"
    session = "" # input("Enter legislative session (leave blank for all sessions): ").strip() or None
    
    size = 1
    #keyword = "cryptocurrency"
    #keyword = "blockchain basics"
    #keyword = "financial innovation"
    #keyword = "depository"
    #keyword = "blockchain"
    #keyword = "digital payment platform"
    keyword = "LC 2211"
    jurisdiction = "Texas"
    # session = "2024"
    print(f"Searching for bills with keyword '{keyword}'...")

    bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
    size = len(bills)
    print("return size = " + str(size))



if __name__ == "__main__":
    main()