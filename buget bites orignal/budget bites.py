

# Budget Bites Lahore
# Programming Fundamentals Project



#User Registration

print("WELCOME TO BUDGET BITES LAHORE")

user_name = input("Enter your name: ")

user_password = input("Create a password: ")

print("\nProfile created successfully.")

print("\nLogin Required")

while True:

    password = input("Enter your password: ")

    if password == user_password:
        print("Login successful.")
        break

    else:
        print("Incorrect password. Try again.")


# ---------- Restaurant Database ----------

restaurants = {

"Monal Lahore":"Liberty Roundabout, Gulberg III",

"Haveli Restaurant":"Fort Road Food Street",

"Spice Bazaar":"MM Alam Road, Gulberg",

"Andaaz Restaurant":"Fort Road Food Street",

"Salt'n Pepper Village":"Liberty Market, Gulberg",

"Arcadian Cafe":"Packages Mall, Walton Road",

"Cafe Aylanto":"MM Alam Road, Gulberg",

"Bundu Khan":"Multiple Branches",

"Butt Karahi":"Lakshmi Chowk",

"Waqas Biryani":"Township",

"Master Biryani":"Johar Town",

"Shawarma Stop":"DHA Phase 4",

"Karachi Red Rock":"DHA Phase 4",

"Mandi House":"Johar Town",

"Dogar Sajji":"Faisal Town",

"KFC":"Multiple Branches",

"McDonald's":"Multiple Branches",

"Hardee's":"Gulberg",

"OPTP":"DHA Phase 5",

"Johnny & Jugnu":"DHA Phase 4",

"Quetta Paratha Hotel":"Liberty Market",

"Chaye Khana":"Gulberg",

"Tuscany Courtyard":"Gulberg",

"PF Chang's":"Packages Mall",

"Cafe Zouk":"MM Alam Road",

"Burger Lab":"Gulberg",

"Ranchers":"Johar Town",

"Howdy":"Gulberg",

"Tabaq Restaurant":"Johar Town",

"Anarkali Food Street":"Anarkali Bazaar",

"Gawalmandi Food Street":"Gawalmandi",

"Sadiq Halwa Puri":"Mozang",

"Arif Chatkhara":"Anarkali",

"Khan Baba Tikka":"Gawalmandi",

"Pizza Hut":"Multiple Branches",

"Broadway Pizza":"Johar Town",

"Nishat Hotel":"Johar Town",

"PC Hotel Lahore":"Mall Road",

"Avari Hotel":"Mall Road",

"Defence Raya Club":"DHA Phase 6"

}


# Juice Points

juice_points = {

"Juice Land":"Johar Town",

"Freshly Juice Bar":"Gulberg",

"Madni Juice":"Anarkali",

"Pulp Juice Bar":"DHA Phase 4",

"Fruiti O":"Johar Town",

"The Juice Company":"DHA Phase 5",

"Al Madina Juice":"Liberty Market",

"Chaman Ice Cream and Juice":"Beadon Road"

}


# ---------- Function 1 ----------

def show_restaurants():

    print("\nRestaurants in Lahore\n")

    for name, location in restaurants.items():

        print(name, "-", location)


# Function 2

def search_restaurant():

    restaurant_name = input("\nEnter restaurant name: ")

    found = False

    for name, location in restaurants.items():

        if restaurant_name.lower() == name.lower():

            print("\nLocation:")

            print(name, "-", location)

            found = True

            break

    if found == False:

        print("Restaurant not found.")


# Function 3


def food_budget():

    budget = int(input("\nEnter your food budget: "))

    print()

    if 250 <= budget <= 500:

        print("Suggested places:")

        print("Anarkali Food Street - Anarkali Bazaar")

        print("Quetta Paratha Hotel - Liberty Market")

        print("Sadiq Halwa Puri - Mozang")

        print("Arif Chatkhara - Anarkali")

        print("Khan Baba Tikka - Gawalmandi")


    elif 500 < budget <= 1000:

        print("Suggested places:")

        print("Master Biryani - Johar Town")

        print("Waqas Biryani - Township")

        print("Bundu Khan - Garden Town")

        print("Hot N Spicy - Faisal Town")

        print("Student Biryani - Gulberg")


    elif 1000 < budget <= 1500:

        print("Suggested places:")

        print("Shawarma Stop - DHA Phase 4")

        print("Karachi Red Rock - DHA Phase 4")

        print("Johnny & Jugnu - DHA Phase 4")

        print("Arcadian Cafe - Packages Mall")

        print("Chaye Khana - Gulberg")


    elif 2000 <= budget <= 2500:

        print("Suggested places:")

        print("KFC - Multiple Branches")

        print("McDonald's - Multiple Branches")

        print("Hardee's - Gulberg")

        print("OPTP - DHA Phase 5")

        print("Burger Lab - Gulberg")


    elif 3000 <= budget <= 3500:

        print("Suggested places:")

        print("Mandi House - Johar Town")

        print("Dogar Sajji - Faisal Town")

        print("Butt Karahi - Lakshmi Chowk")

        print("Tabaq Restaurant - Johar Town")


    elif 4000 <= budget <= 4500:

        print("Suggested places:")

        print("Nishat Hotel Hi Tea - Johar Town")

        print("Ramada Hotel Hi Tea - Gulberg")

        print("Faletti's Hotel Buffet - Egerton Road")


    elif 5000 <= budget <= 5500:

        print("Suggested places:")

        print("PC Hotel Buffet - Mall Road")

        print("Royal Swiss Buffet - Airport Road")

        print("Avari Hotel Buffet - Mall Road")


    elif 6000 <= budget <= 6500:

        print("Suggested places:")

        print("Defence Raya Club - DHA Phase 6")

        print("The Polo Lounge - Defence Raya")

        print("Novu Restaurant - DHA")

    else:

        print("No recommendations available.")


#Function 4

def juice_budget():

    budget = int(input("\nEnter your drinks budget: "))

    print()

    if 100 <= budget <= 250:

        print("Madni Juice - Anarkali")

        print("Chaman Ice Cream and Juice - Beadon Road")

    elif 250 < budget <= 500:

        print("Juice Land - Johar Town")

        print("Al Madina Juice - Liberty Market")

    elif 500 < budget <= 800:

        print("Freshly Juice Bar - Gulberg")

        print("Fruiti O - Johar Town")

    elif 800 < budget <= 1200:

        print("Pulp Juice Bar - DHA Phase 4")

        print("The Juice Company - DHA Phase 5")

    else:

        print("No recommendations available.")


# Function 5

def view_profile():

    hidden_password = "*" * len(user_password)

    print("\nUser Profile")

    print("Name:", user_name)

    print("Password:", hidden_password)


# Main Menu

while True:

    print("\n BUDGET BITES LAHORE ")

    print("1. Access All Restaurants")

    print("2. Search Restaurant Location")

    print("3. Food Recommendations According To Budget")

    print("4. Juice Points According To Budget")

    print("5. View User Profile")

    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        show_restaurants()


    elif choice == "2":

        search_restaurant()


    elif choice == "3":

        food_budget()


    elif choice == "4":

        juice_budget()


    elif choice == "5":

        view_profile()


    elif choice == "6":

        print("Thank you for using Budget Bites Lahore.")

        break


    else:

        print("Invalid choice.")


