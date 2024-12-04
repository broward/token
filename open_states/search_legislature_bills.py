import requests
import json
import sys

file = open('/home/tyche/Downloads/api_key.json', "r")
API_KEY = file.read().strip()
print(API_KEY)
file.close()

# Open States API Key
# API_KEY = "YOUR_API_KEY"

# Base URLs for Open States API
BASE_BILLS_URL = "https://v3.openstates.org/bills/"
BASE_PEOPLE_URL = "https://v3.openstates.org/people/"

def search_bills_by_keyword(keyword, jurisdiction="all", session=None):
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
        "page": 1,
        "per_page": 20,
        # "jurisdiction": jurisdiction,
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
            session = bill.get("session", "no session available")
            subjects = bill.get("subject", [])
            sponsors = bill.get("sponsorships", [])
            
            # Collect sponsor names and IDs
            sponsor_details = [
                {"name": sponsor.get("name"), "id": sponsor.get("id")}
                for sponsor in sponsors
            ]
            
            results.append({
                "jurisdiction": jurisdiction,
                "title": title,
                "session": session,
                "subjects": subjects,
                "sponsors": sponsor_details
            })
        
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
    keyword = input("Enter a keyword or phrase to search in bill titles and subjects: ").strip()
    jurisdiction = input("Enter jurisdiction (default is 'all'): ").strip() or "all"
    session = input("Enter legislative session (leave blank for all sessions): ").strip() or None
    
    print(f"Searching for bills with keyword '{keyword}'...")
    bills = search_bills_by_keyword(keyword, jurisdiction, session)
    
    if bills:
        print(f"Found {len(bills)} bills:")
        for bill in bills:
            print(f"\nTitle: {bill['title']}")
            print(f"Jurisdiction: {bill.get('jurisdiction', {}).get('name', 'Unknown')}")
            print(f"Session: {bill['session']}")
            print(f"Subjects: {', '.join(bill['subjects']) if bill['subjects'] else 'None'}")
            if bill["sponsors"]:
                print("Sponsors:")
                for sponsor in bill["sponsors"]:
                    print(f"  - Name: {sponsor['name']} (ID: {sponsor['id']})")
            else:
                print("Sponsors: None")
    else:
        print("No bills found.")
    
    # Optionally fetch sponsor details
    sponsor_id = input("\nEnter a sponsor ID to fetch detailed information (or leave blank to exit): ").strip()
    if sponsor_id:
        sponsor_details = get_sponsor_details(sponsor_id)
        print("\nSponsor Details:")
        print(sponsor_details)

if __name__ == "__main__":
    main()
