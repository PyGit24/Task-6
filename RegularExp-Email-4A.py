# Regular Expression in Email validation using Regex
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid Email")
    else:
      print("Invalid Email")
email= "varman.lic010@gmail.com"
print("\tProgram to find Valid & Invalid Email")
print("The Given Email id is:",email)
isValid(email)