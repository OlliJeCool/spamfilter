import email
from bs4 import BeautifulSoup
from ..corpus import Corpus

# temp file name this is
c = Corpus("1")
msg = email.message_from_string(next(c.emails())[1])

# Initialize variables to store content
plain_text = ""
html_content = ""

# Loop through the parts of the email to extract plain text and HTML
for part in msg.walk():
    content_type = part.get_content_type()
    
    # Use 'utf-8' as fallback charset if it's not provided or invalid
    charset = part.get_content_charset()
    if not charset:
        charset = "utf-8"  # Fallback encoding
    
    try:
        if content_type == "text/html":
            html_content = part.get_payload(decode=True).decode(charset, 'ignore')
        elif content_type == "text/plain":
            plain_text = part.get_payload(decode=True).decode(charset, 'ignore')
    except LookupError:
        # Handle unknown encodings gracefully
        print(f"Unknown encoding: {charset}. Using utf-8 as fallback.")
        if content_type == "text/html":
            html_content = part.get_payload(decode=True).decode('utf-8', 'ignore')
        elif content_type == "text/plain":
            plain_text = part.get_payload(decode=True).decode('utf-8', 'ignore')

# If there's HTML content, parse it with BeautifulSoup
if html_content:
    soup = BeautifulSoup(html_content, "lxml")

    # Extract all the links in the HTML
    links = [link.get('href') for link in soup.find_all('a')]
    print("Links in the email:", links)

    # Extract body text
    body_text = soup.get_text()
    print("Body text in the email:", body_text)

# Optionally print the plain text part if available
if plain_text:
    print("Plain Text:", plain_text)
