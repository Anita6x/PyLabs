import re
import os

with open("myname.txt") as file:
    full_name = file.read().strip()


match = re.match(r'(\w+)\s+(\w+)\s+(\w+)', full_name)

if match:
    first_name = match.group(1)
    middle_name = match.group(2)
    last_name = match.group(3)

    print("First Name:", first_name)
    print("Middle Name:", middle_name)
    print("Last Name:", last_name)
else:
    print("Name format not recognized.")
    
full_path = os.getcwd()
print("full path to file:", full_path)