# lib/email_address_parser.py
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split string on commas or whitespace
        split_addresses = re.split(r"[,\s]+", self.addresses.strip())

        # Filter only valid email addresses using regex
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        emails = [email for email in split_addresses if re.fullmatch(email_pattern, email)]

        # Return unique addresses sorted alphabetically
        return sorted(set(emails))
