try:
    # Input bio data
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    contact = input("Enter Contact Number: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female): ").lower()

    # Validate Name
    if any(char.isdigit() for char in name):
        raise Exception("Name should not contain digits.")

    # Validate Address
    if len(address) < 3:
        raise Exception("Address must be at least 3 characters long.")

    # Validate Contact Number
    if any(char.isalpha() for char in contact):
        raise Exception("Contact number should not contain alphabets.")

    # Validate Age
    if age < 0 or age > 150:
        raise Exception("Age must be between 0 and 150.")

    # Validate Gender
    if gender not in ["male", "female"]:
        raise Exception("Gender must be either Male or Female.")

    print("\nBio Data is Valid.")
    print("Name:", name)
    print("Address:", address)
    print("Contact Number:", contact)
    print("Age:", age)
    print("Gender:", gender.capitalize())

except ValueError:
    print("Error: Age must be a valid integer.")

except Exception as e:
    print("Error:", e)