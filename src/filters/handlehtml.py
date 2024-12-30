import email
import re
from src.corpus import Corpus

# temp file name this is
def handlehtml(path):
    c = Corpus(path)
    msg = email.message_from_string(next(c.emails())[1])

    # Initialize variables to store content
    plain_text = ""
    html_content = ""

    # Regex patterns for extracting links and body text
    link_pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"')
    body_text_pattern = re.compile(r'<body[^>]*>(.*?)</body>', re.DOTALL)

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

    # If there's HTML content, use regex to extract links and body text
    if html_content:
        # Extract all the links in the HTML
        links = link_pattern.findall(html_content)
        # print("Links in the email:", links) print links in the email

        # Extract body content (between <body> and </body> tags)
        body_match = body_text_pattern.search(html_content)
        body_text = ""
        if body_match:
            body_text = re.sub(r'<[^>]+>', '', body_match.group(1))  # Remove all HTML tags
        # print("Body text in the email:", body_text) print body text in the email
        return body_text

    # Optionally print the plain text part if available
    if plain_text:
        # print("Plain Text:", plain_text) print plain text
        return plain_text
