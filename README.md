# Email OSINT Tool

![image](https://github.com/user-attachments/assets/2c17f75a-80ac-4df5-a420-abccc8275bad)


## Description

The **Email OSINT Tool** is a Python script designed to perform **Open-Source Intelligence (OSINT)** checks on email addresses. The tool provides various checks, such as verifying email format, identifying disposable email providers, checking if the email has been involved in data breaches, performing WHOIS lookups on the email's domain, and analyzing the email's reputation.

This tool is useful for security professionals, investigators, and anyone wanting to gather information about an email address.

## Features

- **Email Format Validation**: Verifies whether the email address follows the correct format.
- **Disposable Email Detection**: Identifies if the email address is from a disposable email provider (e.g., `mailinator.com`, `10minutemail.com`).
- **Data Breach Detection**: Checks if the email address has been involved in known data breaches using the **Have I Been Pwned API**.
- **WHOIS Domain Lookup**: Retrieves WHOIS information for the domain of the email (e.g., domain registration details, creation date, etc.).
- **Email Reputation Check**: Uses an external API to evaluate the reputation and risk of the email address.

## Requirements

- **Python 3.x**: Ensure Python 3.x is installed on your machine.
- **External Libraries**:
  - `whois`: To fetch WHOIS information for the domain.
  - `requests`: For sending HTTP requests to the APIs.
  - `re`: To validate the email format with regular expressions.

## How to use

**1. Install Dependencies**
Make sure you have installed the necessary Python libraries (whois and requests). You can do this by running:

```bash
sudo apt update && upgrade
sudo apt install python3
pip install whois requests
git clone https://github.com/your-username/email-osint-tool.git
cd email-osint
python3 email_osint.py
```

## The tool will display the following details:

**Email Format Check:** Whether the email is in a valid format.
**Disposable Email Check:** A warning if the email is from a disposable provider.
**Breach Detection:** Whether the email has been involved in known data breaches.
**WHOIS Domain Information:** Information about the domain associated with the email address (e.g., registration date, domain age).
**Email Reputation:** A reputation score and risk level for the email address.bash
## Limitations
The **Have I Been Pwned** API is rate-limited, meaning too many requests in a short period may result in temporary blocks.
The **Eva PingUtil** API may require API keys or could have usage restrictions.
The list of disposable email providers is static and may require updates over time to include new services.
## Disclaimer
Use responsibly: This tool is intended for ethical use and educational purposes only. 
Always ensure you have explicit permission to perform any OSINT on email addresses that do not belong to you. 
Unauthorized access to or misuse of this tool could violate laws or regulations in your jurisdiction.
