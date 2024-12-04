import requests
import json
import sys, os

# Open States API Key
file = open('/home/tyche/Downloads/api_key.json', "r")
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
        "updated_at": "2024-06-04T02:43:14.396Z",
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

            print(str(sponsors))
            
            # Collect sponsor names and IDs
            sponsor_details = [
                {"name": sponsor.get("name"), "id": sponsor.get("id")}
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
                with open("pending_legislation.txt", "a") as f:
            
                    print(str(results))
                    f.write(f"Found {len(results)} bills:")
                    for result in results:
                        f.write(f"\n\nTitle: {result['title']}")
                        f.write(f"\nJurisdiction: {result['jurisdiction']['name']}")
                        f.write(f"\nIdentifier: {result['identifier']}")
                        f.write("\n")
                        # f.write(f"\nUpdated: {result['updated']}")
                        # f.write(f"\nSponsor: {result['sponsor']}")
                        # f.write(f"\nSubjects: {', '.join(result['subjects']) if result['subjects'] else 'None'}")
                        # if result["sponsors"]:
                        #    f.write("\nSponsors:")
                        #    for sponsor in result["sponsors"]:
                        #        f.write(f"  - Name: {sponsor['name']} (ID: {sponsor['id']})")
                        #else:
                        #    f.write("\nSponsors: None")
            else:
                print(" Sponsors: None")
        else:
            print(" No bills found.")

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return []

def get_sponsor_details(sponsor_id):
    """
    Retrieves detailed information about a sponsor by their ID.

    Args:
        sponsor_id (str): The sponsor's unique ID.

    Returns:
        dict: Detailed information about the sponsor.
    """
    url = f"{BASE_PEOPLE_URL}{sponsor_id}/"
    params = {"apikey": API_KEY}
    
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
    while size > 0:
        keyword = "gold state depository"
        print(f"Searching for bills with keyword '{keyword}'...")

        bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
        size = len(bills)
        print("return size = " + str(size))

    size = 1
    while size > 0:
        keyword = "bullion depository"
        print(f"Searching for bills with keyword '{keyword}'...")

        bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
        size = len(bills)
        print("return size = " + str(size))

    size = 1
    while size > 0:
        keyword = "precious metals depository"
        print(f"Searching for bills with keyword '{keyword}'...")

        bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
        size = len(bills)
        print("return size = " + str(size))

    size = 1
    while size > 0:
        keyword = "precious metals digital currency"
        print(f"Searching for bills with keyword '{keyword}'...")

        bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
        size = len(bills)
        print("return size = " + str(size))

        size = 1
    while size > 0:
        keyword = "blockchain platform"
        print(f"Searching for bills with keyword '{keyword}'...")

        bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
        size = len(bills)
        print("return size = " + str(size))

    size = 1
    while size > 0:
        keyword = "digital currency platform"
        print(f"Searching for bills with keyword '{keyword}'...")

        bills = search_bills_by_keyword(size, keyword, jurisdiction, session)
        size = len(bills)
        print("return size = " + str(size))

if __name__ == "__main__":
    main()
