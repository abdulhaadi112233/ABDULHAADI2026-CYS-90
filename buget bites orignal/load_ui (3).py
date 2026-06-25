

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


# Restaurant Database

restaurants = {
    "Monal Lahore": "Liberty Roundabout, Gulberg III",
    "Haveli Restaurant": "Fort Road Food Street",
    "Spice Bazaar": "MM Alam Road, Gulberg",
    "Andaaz Restaurant": "Fort Road Food Street",
    "Salt'n Pepper Village": "Liberty Market, Gulberg",
    "Arcadian Cafe": "Packages Mall, Walton Road",
    "Cafe Aylanto": "MM Alam Road, Gulberg",
    "Bundu Khan": "Multiple Branches",
    "Butt Karahi": "Lakshmi Chowk",
    "Waqas Biryani": "Township",
    "Master Biryani": "Johar Town",
    "Shawarma Stop": "DHA Phase 4",
    "Karachi Red Rock": "DHA Phase 4",
    "Mandi House": "Johar Town",
    "Dogar Sajji": "Faisal Town",
    "KFC": "Multiple Branches",
    "McDonald's": "Multiple Branches",
    "Hardee's": "Gulberg",
    "OPTP": "DHA Phase 5",
    "Johnny & Jugnu": "DHA Phase 4",
    "Quetta Paratha Hotel": "Liberty Market",
    "Chaye Khana": "Gulberg",
    "Tuscany Courtyard": "Gulberg",
    "PF Chang's": "Packages Mall",
    "Cafe Zouk": "MM Alam Road",
    "Burger Lab": "Gulberg",
    "Ranchers": "Johar Town",
    "Howdy": "Gulberg",
    "Tabaq Restaurant": "Johar Town",
    "Anarkali Food Street": "Anarkali Bazaar",
    "Gawalmandi Food Street": "Gawalmandi",
    "Sadiq Halwa Puri": "Mozang",
    "Arif Chatkhara": "Anarkali",
    "Khan Baba Tikka": "Gawalmandi",
    "Pizza Hut": "Multiple Branches",
    "Broadway Pizza": "Johar Town",
    "Nishat Hotel": "Johar Town",
    "PC Hotel Lahore": "Mall Road",
    "Avari Hotel": "Mall Road",
    "Defence Raya Club": "DHA Phase 6",
}

# Juice Points ()

juice_points = {
    "Juice Land": "Johar Town",
    "Freshly Juice Bar": "Gulberg",
    "Madni Juice": "Anarkali",
    "Pulp Juice Bar": "DHA Phase 4",
    "Fruiti O": "Johar Town",
    "The Juice Company": "DHA Phase 5",
    "Al Madina Juice": "Liberty Market",
    "Chaman Ice Cream and Juice": "Beadon Road",
}


class BudgetBitesApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # User state (replaces the global user_name / user_password in the
        # original script)
        self.user_name = ""
        self.user_password = ""
        self.is_registered = False  # tracks whether Sign Up has happened yet

        # Load the main window shell (contains the QStackedWidget)
        uic.loadUi("main_window.ui", self)

        # Load each screen's .ui into a widget object, then swap it
        # into the corresponding placeholder page in the stack.
        self.auth_screen = uic.loadUi("auth_screen.ui")
        self.main_menu_screen = uic.loadUi("main_menu.ui")
        self.restaurants_screen = uic.loadUi("restaurants_screen.ui")
        self.budget_screen = uic.loadUi("budget_screen.ui")

        self.stackedWidget.insertWidget(0, self.auth_screen)
        self.stackedWidget.insertWidget(1, self.main_menu_screen)
        self.stackedWidget.insertWidget(2, self.restaurants_screen)
        self.stackedWidget.insertWidget(3, self.budget_screen)

        # Remove the original empty placeholder pages (now at indices 4-7)
        for _ in range(4):
            self.stackedWidget.removeWidget(self.stackedWidget.widget(4))

        self.stackedWidget.setCurrentIndex(0)  # start on Auth screen

        # Start on the Sign Up tab since there's no account yet
        # (tab index 1 = "Sign Up" in auth_screen.ui)
        self.auth_screen.tabWidget_auth.setCurrentIndex(1)

        # ---------------- Navigation / logic wiring ----------------

        self.auth_screen.pushButton_login.clicked.connect(self.handle_login)
        self.auth_screen.pushButton_signup.clicked.connect(self.handle_signup)

        self.main_menu_screen.pushButton_navRestaurants.clicked.connect(
            self.open_restaurants_screen
        )
        self.main_menu_screen.pushButton_navBudget.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3)
        )
        self.main_menu_screen.pushButton_navProfile.clicked.connect(
            self.view_profile
        )
        self.main_menu_screen.pushButton_navExit.clicked.connect(
            self.handle_exit
        )

        self.restaurants_screen.pushButton_backFromRestaurants.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
        self.budget_screen.pushButton_backFromBudget.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )

        self.restaurants_screen.lineEdit_searchRestaurant.textChanged.connect(
            self.filter_restaurants
        )

        self.budget_screen.pushButton_getFoodSuggestions.clicked.connect(
            self.get_food_suggestions
        )
        self.budget_screen.pushButton_getDrinksSuggestions.clicked.connect(
            self.get_drinks_suggestions
        )


    # Auth logic (replaces the registration + login while-loop)


    def handle_signup(self):
        name = self.auth_screen.lineEdit_signupName.text().strip()
        password = self.auth_screen.lineEdit_signupPassword.text()

        if not name or not password:
            QMessageBox.warning(
                self, "Missing Info", "Please enter both a name and a password."
            )
            return

        self.user_name = name
        self.user_password = password
        self.is_registered = True

        QMessageBox.information(self, "Success", "Profile created successfully.")

        # Clear fields and switch to Login tab, like the original script
        # moving straight from registration into "Login Required"
        self.auth_screen.lineEdit_signupName.clear()
        self.auth_screen.lineEdit_signupPassword.clear()
        self.auth_screen.tabWidget_auth.setCurrentIndex(0)  # Login tab

    def handle_login(self):
        if not self.is_registered:
            QMessageBox.warning(
                self, "No Account", "Please sign up first before logging in."
            )
            self.auth_screen.tabWidget_auth.setCurrentIndex(1)
            return

        entered_password = self.auth_screen.lineEdit_password.text()

        if entered_password == self.user_password:
            self.auth_screen.label_loginError.setVisible(False)
            self.auth_screen.lineEdit_password.clear()
            self.stackedWidget.setCurrentIndex(1)  # go to Main Menu
        else:
            # Same behaviour as: print("Incorrect password. Try again.")
            self.auth_screen.label_loginError.setVisible(True)


    # Function 1: show_restaurants() -> populate Restaurants screen


    def open_restaurants_screen(self):
        self.restaurants_screen.lineEdit_searchRestaurant.clear()
        self.populate_restaurant_list(restaurants)
        self.stackedWidget.setCurrentIndex(2)

    def populate_restaurant_list(self, data_dict):
        self.restaurants_screen.listWidget_restaurants.clear()
        for name, location in data_dict.items():
            self.restaurants_screen.listWidget_restaurants.addItem(
                f"{name} - {location}"
            )
        self.restaurants_screen.label_restaurantNotFound.setVisible(
            len(data_dict) == 0
        )


    # Function 2: search_restaurant()


    def filter_restaurants(self, text):
        restaurant_name = text.strip()

        if restaurant_name == "":
            # Empty search box -> show full list again
            self.populate_restaurant_list(restaurants)
            return

        found_items = {}
        search_text = restaurant_name.lower()
        for name, location in restaurants.items():
            if search_text in name.lower():
                found_items[name] = location

        if found_items:
            self.populate_restaurant_list(found_items)
        else:
            self.restaurants_screen.listWidget_restaurants.clear()
            self.restaurants_screen.label_restaurantNotFound.setVisible(True)


    # Function 3: food_budget() -> exact same budget ranges


    def get_food_suggestions(self):
        budget = self.budget_screen.spinBox_foodBudget.value()
        self.budget_screen.listWidget_foodSuggestions.clear()

        if 250 <= budget <= 500:
            suggestions = [
                ("Anarkali Food Street", "Anarkali Bazaar"),
                ("Quetta Paratha Hotel", "Liberty Market"),
                ("Sadiq Halwa Puri", "Mozang"),
                ("Arif Chatkhara", "Anarkali"),
                ("Khan Baba Tikka", "Gawalmandi"),
            ]
        elif 500 < budget <= 1000:
            suggestions = [
                ("Master Biryani", "Johar Town"),
                ("Waqas Biryani", "Township"),
                ("Bundu Khan", "Garden Town"),
                ("Hot N Spicy", "Faisal Town"),
                ("Student Biryani", "Gulberg"),
            ]
        elif 1000 < budget <= 1500:
            suggestions = [
                ("Shawarma Stop", "DHA Phase 4"),
                ("Karachi Red Rock", "DHA Phase 4"),
                ("Johnny & Jugnu", "DHA Phase 4"),
                ("Arcadian Cafe", "Packages Mall"),
                ("Chaye Khana", "Gulberg"),
            ]
        elif 2000 <= budget <= 2500:
            suggestions = [
                ("KFC", "Multiple Branches"),
                ("McDonald's", "Multiple Branches"),
                ("Hardee's", "Gulberg"),
                ("OPTP", "DHA Phase 5"),
                ("Burger Lab", "Gulberg"),
            ]
        elif 3000 <= budget <= 3500:
            suggestions = [
                ("Mandi House", "Johar Town"),
                ("Dogar Sajji", "Faisal Town"),
                ("Butt Karahi", "Lakshmi Chowk"),
                ("Tabaq Restaurant", "Johar Town"),
            ]
        elif 4000 <= budget <= 4500:
            suggestions = [
                ("Nishat Hotel Hi Tea", "Johar Town"),
                ("Ramada Hotel Hi Tea", "Gulberg"),
                ("Faletti's Hotel Buffet", "Egerton Road"),
            ]
        elif 5000 <= budget <= 5500:
            suggestions = [
                ("PC Hotel Buffet", "Mall Road"),
                ("Royal Swiss Buffet", "Airport Road"),
                ("Avari Hotel Buffet", "Mall Road"),
            ]
        elif 6000 <= budget <= 6500:
            suggestions = [
                ("Defence Raya Club", "DHA Phase 6"),
                ("The Polo Lounge", "Defence Raya"),
                ("Novu Restaurant", "DHA"),
            ]
        else:
            suggestions = []

        if suggestions:
            for name, location in suggestions:
                self.budget_screen.listWidget_foodSuggestions.addItem(
                    f"{name} - {location}"
                )
        else:
            self.budget_screen.listWidget_foodSuggestions.addItem(
                "No recommendations available."
            )


    # Function 4: juice_budget() -> exact same budget ranges


    def get_drinks_suggestions(self):
        budget = self.budget_screen.spinBox_drinksBudget.value()
        self.budget_screen.listWidget_drinksSuggestions.clear()

        if 100 <= budget <= 250:
            suggestions = [
                ("Madni Juice", "Anarkali"),
                ("Chaman Ice Cream and Juice", "Beadon Road"),
            ]
        elif 250 < budget <= 500:
            suggestions = [
                ("Juice Land", "Johar Town"),
                ("Al Madina Juice", "Liberty Market"),
            ]
        elif 500 < budget <= 800:
            suggestions = [
                ("Freshly Juice Bar", "Gulberg"),
                ("Fruiti O", "Johar Town"),
            ]
        elif 800 < budget <= 1200:
            suggestions = [
                ("Pulp Juice Bar", "DHA Phase 4"),
                ("The Juice Company", "DHA Phase 5"),
            ]
        else:
            suggestions = []

        if suggestions:
            for name, location in suggestions:
                self.budget_screen.listWidget_drinksSuggestions.addItem(
                    f"{name} - {location}"
                )
        else:
            self.budget_screen.listWidget_drinksSuggestions.addItem(
                "No recommendations available."
            )


    # Function 5: view_profile()


    def view_profile(self):
        hidden_password = "*" * len(self.user_password)
        QMessageBox.information(
            self,
            "User Profile",
            f"Name: {self.user_name}\nPassword: {hidden_password}",
        )


    # Exit (replaces choice == "6")


    def handle_exit(self):
        QMessageBox.information(
            self, "Goodbye", "Thank you for using Budget Bites Lahore."
        )
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BudgetBitesApp()
    window.show()
    sys.exit(app.exec_())
