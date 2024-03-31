# Passwod Pattern Validation - Minimum Sixteen characters, at least one uppercase letter, 
# one lowercase letter, one number and one special character:

import re

def validate_password(regex, pword):
    match = re.search(regex, pword)
    if match:
        return "Password Pattern is Valid"
    return "Password Pattern is InValid"

pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{16,}$")

test_passwords = [
    "Alph$20456$Beta!",
    "Gamma-55-123$467",
    "Gamma*55?123%467",
    "+44 (0) 20 1234 5678",
    "02012345678",   ]

for number in test_passwords:
    print("\tRegular Expression Python Program to Validate 16 Character Password Pattern")
    print(f"{number} -- {validate_password(pattern, number)}\n")