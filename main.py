import whois  # Ensure this is python-whois
import requests

def check_email_breach(email):
    """Check if the email has been involved in a data breach using the Have I Been Pwned API."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    
    headers = {
        'User-Agent': 'Email OSINT Script',
        # 'hibp-api-key': 'YOUR_API_KEY'  # Add your API key here if necessary
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            print(f"\nThe email '{email}' has been found in the following breaches:")
            for breach in breaches:
                print(f"- {breach['Name']} (Breach Date: {breach['BreachDate']})")
        elif response.status_code == 404:
            print(f"\nThe email '{email}' has not been found in any breaches.")
        else:
            print(f"Error checking breaches: {response.status_code}")
    except Exception as e:
        print(f"\nAn error occurred while checking breaches: {e}")

def get_domain_info(email):
    """Get WHOIS information for the domain of the email."""
    domain = email.split('@')[1]
    try:
        # Make sure you have 'python-whois' installed and use the correct function
        domain_info = whois.whois(domain)
        print(f"\nWHOIS information for domain '{domain}':")
        print(f"Domain Name: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Name Servers: {domain_info.name_servers}")
    except Exception as e:
        print(f"\nAn error occurred while fetching domain info for '{domain}': {e}")

def main():
    email = input("Enter an email address to perform OSINT: ").strip()
    get_domain_info(email)
    check_email_breach(email)

if __name__ == "__main__":
    main()
