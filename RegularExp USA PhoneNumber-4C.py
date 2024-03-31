# Valid USA Phone number
import re

def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return "Valid USA Phone Number"
    return "Not a Valid USA Phone Number"

pattern = re.compile(r"(\+1)?\s?\(?(2\d{2}|[3-9]\d{2})\)?[\s.-]?\d{3}[\s.-]?\d{4}")

test_phone_numbers = [
    "+1 (555) 123-4567",
    "555-123-4567",
    "555 123 4567",
    "+44 (0) 20 1234 5678",
    "02012345678",
    "invalid phone number" ]

for number in test_phone_numbers:
    print("\tProgram to Find Telephone Numbers of USA")
    print(f"{number}: {validate_phone_number(pattern, number)}\n")