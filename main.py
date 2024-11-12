# def greatest_number(numbers):
    
#     print(max(numbers))
     

# user_input = input("enter the numbers seperated by spaces")
# numbers = [int(num) for num in user_input.split()]
# greatest_number(numbers)



# 

# word_meanings = {
#     "tables": "a piece of furnitures " "list of fact and figures",
#     "cat": "a small animal"

# }

# print(word_meanings["tables"])



import whois
import requests
import re
from datetime import datetime

# List of disposable email providers
DISPOSABLE_EMAIL_PROVIDERS = [
    "mailinator.com", "10minutemail.com", "tempmail.com", "guerrillamail.com",
    "yopmail.com", "throwawaymail.com", "temp-mail.org", "getnada.com"
]

def check_email_format(email):
    """Check if the email address is valid."""
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def check_email_provider(email):
    """Identify the email service provider."""
    return email.split('@')[1]

def check_disposable_email(email):
    """Check if the email is from a disposable email provider."""
    domain = email.split('@')[1]
    return domain in DISPOSABLE_EMAIL_PROVIDERS

def check_email_breach(email):
    """Check if the email has been involved in a data breach using the Have I Been Pwned API."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        'User -Agent': 'Email OSINT Script',
        # 'hibp-api-key': 'YOUR_API_KEY'  # Uncomment and add your API key if necessary
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
        domain_info = whois.whois(domain)
        print(f"\nWHOIS information for domain '{domain}':")
        print(f"Domain Name: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Name Servers: {domain_info.name_servers}")

        # Calculate the age of the domain
        if domain_info.creation_date:
            if isinstance(domain_info.creation_date, list):
                creation_date = domain_info.creation_date[0]
            else:
                creation_date = domain_info.creation_date
            domain_age = (datetime.now() - creation_date).days
            print(f"Domain Age: {domain_age} days")
    except Exception as e:
        print(f"\nAn error occurred while fetching domain info for '{domain}': {e}")

def check_email_reputation(email):
    """Check the reputation of the email address using an external API."""
    
    
    try:
        response = requests.get(f"https://api.eva.pingutil.com/email?email={email}")
        if response.status_code == 200:
            data = response.json()
            print(f"\nReputation for '{email}':")
            print(f"Reputation: {data.get('reputation', 'N/A')}")
            print(f"Risk: {data.get('risk', 'N/A')}")
            print(f"Last Seen: {data.get('last_seen', 'N/A')}")
        else:
            print(f"Error checking reputation: {response.status_code}")
    except Exception as e:
        print(f"\nAn error occurred while checking email reputation: {e}")

def main():
    email = input("Enter an email address to perform OSINT: ").strip()

    if not check_email_format(email):
        print("Invalid email format.")
        return

    provider = check_email_provider(email)
    print(f"Email Provider: {provider}")

    if check_disposable_email(email):
        print("Warning: This email address is from a disposable email provider.")

    get_domain_info(email)
    check_email_breach(email)
    check_email_reputation(email )

if __name__ == "__main__":
    main()
