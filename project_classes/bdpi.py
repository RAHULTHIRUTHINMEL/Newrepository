import math

# Enter your birthday as 'dd/mm' format
birthday = input("Enter your birthday in 'dd/mm' format: ")

# Generate pi value as a string
pi_str = str(math.pi)

# Remove decimal point from pi string
pi_str = pi_str.replace(".", "")

# Iterate through each digit of pi string
for i in range(len(pi_str) - len(birthday)):
    # Check if consecutive digits match birthday
    if pi_str[i:i+len(birthday)] == birthday:
        # Found a match!
        print("Your birthday appears in consecutive digits of pi, starting at position", i+1)
        break
else:
    # No match found
    print("Sorry, your birthday does not appear in consecutive digits of pi.")
