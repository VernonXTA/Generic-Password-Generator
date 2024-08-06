import random
import string

def random_password_generator(length=30, include_upper=True, include_lower=True, include_digits=True, include_punctuation=True):
    if not (include_upper or include_lower or include_digits or include_punctuation):
        raise ValueError("At least one character set must be included.")

    password_characters = ""
    if include_upper:
        password_characters += string.ascii_uppercase
    if include_lower:
        password_characters += string.ascii_lowercase
    if include_digits:
        password_characters += string.digits
    if include_punctuation:
        password_characters += string.punctuation

    if len(password_characters) == 0:
        raise ValueError("No characters available for password generation.")


    """" ENSURES THAT THE PASSWORD IS APPENDING UPPERCASE, LOWERCASE, DIGITS AND PUNCTUATION 
            Will continue to edit the password and ensure that all settings are working"""
    password = []
    if include_upper:
        password.append(random.choice(string.ascii_uppercase))
    if include_lower:
        password.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_punctuation:
        password.append(random.choice(string.punctuation))

    password += [random.choice(password_characters) for _ in range(length - len(password))]

    random.shuffle(password)

    return ''.join(password)

"""" ESTABLISH THE BASELINE TO PRINT THE PASSWORD 
        Do not edit the settings besides the integer.
"""
savedFile = random_password_generator(30, include_upper=True, include_lower=True, include_digits=True, include_punctuation=True)

def determineSave(password):
    userInput = input("Do you wish to save this password? (Yes/Y | No/N): ")
    fileName = "GeneratedPassword"
    if userInput in ['Y', 'Yes', 'yes']:
        with open(f"{fileName}.txt", "w") as file:
            file.write(password)
        print(f"Password saved to {fileName}.txt")
    else:
        print(savedFile)

# Generate the password
savedFile = random_password_generator(30, include_upper=True, include_lower=True, include_digits=True, include_punctuation=True)

# Call the function to save the password
determineSave(savedFile)