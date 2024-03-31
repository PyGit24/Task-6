# Validate Bangaladesh Phone number
import re

def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return "Valid Bangladesh Phone Number"
    return "Not a Valid Bangladesh Phone Number"

pattern = re.compile(r"(\+\d{1,4})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{8}")

test_phone_numbers = [
    "+8801840001417",
    "555-123-4567",
    "555 123 4567",
    "+44 (0) 20 1234 5678",
    "02012345678",
    "invalid phone number"]

for number in test_phone_numbers:
    print("\tProgram to Find Bangladesh Phone Number")
    print(f"{number} is {validate_phone_number(pattern, number)}\n")