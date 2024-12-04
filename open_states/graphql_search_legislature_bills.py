import requests

# API base URL and token
API_URL = "https://open.pluralpolicy.com/graphql"
# API_KEY = "your_api_key_here"  # Replace with your actual API key
file = open('/home/tyche/Downloads/api_key.json', "r")
API_KEY = file.read().strip()
print(API_KEY)
file.close()

def search_bills(word_or_phrase):
    """
    Searches for bills by a keyword or phrase in title and subject fields.

    Args:
        word_or_phrase (str): The keyword or phrase to search for.

    Returns:
        list: List of bills with their title, subject, sponsorships, and sponsor addresses.
    """
    query = """
    query SearchBills($searchTerm: String!) {
        bills(query: $searchTerm) {
            edges {
                node {
                    title
                    subject
                    sponsorships {
                        edges {
                            node {
                                name
                                contactDetails {
                                    address
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    """
    variables = {"searchTerm": word_or_phrase}
    headers = {"x-api-key": API_KEY}  # Correct header for Plural Policy API

    try:
        response = requests.post(API_URL, json={"query": query, "variables": variables}, headers=headers)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        data = response.json()
        return data.get("data", {}).get("bills", {}).get("edges", [])
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return []

def main():
    # Input from user
    search_term = input("Enter a word or phrase to search for in bills: ").strip()
    if not search_term:
        print("Search term cannot be empty!")
        return
    
    print(f"Searching bills for the term: {search_term}...")
    bills = search_bills(search_term)
    
    if not bills:
        print("No bills found.")
        return
    
    # Display results
    for bill_edge in bills:
        bill = bill_edge["node"]
        print(f"\nTitle: {bill.get('title', 'No Title')}")
        print(f"Subjects: {', '.join(bill.get('subject', [])) if bill.get('subject') else 'No Subjects'}")
        
        sponsorships = bill.get("sponsorships", {}).get("edges", [])
        if sponsorships:
            print("Sponsorships:")
            for sponsor_edge in sponsorships:
                sponsor = sponsor_edge["node"]
                print(f"  - Name: {sponsor.get('name', 'No Name')}")
                print(f"    Address: {sponsor.get('contactDetails', {}).get('address', 'No Address')}")
        else:
            print("Sponsorships: None")
    print("\nSearch complete!")

if __name__ == "__main__":
    main()
