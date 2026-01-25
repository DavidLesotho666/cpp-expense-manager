# Import the built-in datetime module to handle date parsing and formatting.
import datetime

class ExpenseTracker:
    """
    The ExpenseTracker class manages the financial records.
    It encapsulates all the data and the methods required to add, filter, 
    and summarize expenses. This object-oriented approach keeps the 
    application modular and allows for easy expansion in the future.
    """

    def __init__(self):
        """
        Constructor Method: Initializes the ExpenseTracker object.
        
        This method is called automatically when a new ExpenseTracker instance is created.
        Python Feature Highlight: In Python, we do not need to pre-define the type 
        or size of the list. We use a dynamic array (list) that can hold any data type.
        Here, it will hold dictionaries representing individual expenses.
        """
        # Initialize an empty list that will store all expense dictionaries dynamically.
        self.expenses = []

    def add_expense(self, date_str, amount, category, description):
        """Adds a new expense to the internal list."""
        try:
            # DEBUGGING: Let's see exactly what the terminal is sending to Python
            print(f"DEBUG: Date received: '{date_str}'")
            print(f"DEBUG: Amount received: '{amount}'")

            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            
            expense = {
                "date": date_obj,
                "amount": float(amount),
                "category": category.title(),
                "description": description
            }
            self.expenses.append(expense)
            print(f"* * * Added: {description} (${float(amount):.2f})")
            
        except ValueError as e:
            # THIS WILL PRINT THE REAL ERROR
            print(f" SYSTEM ERROR: {e}")

    def view_all(self):
        """
        Displays all recorded expenses in the tracker.
        
        This is a simple wrapper function that passes the entire internal 
        expense list to the helper printing method. It improves code readability 
        by abstracting the display logic away from the main loop.
        """
        # Call the internal helper method to print the entire list of expenses.
        self._print_expenses(self.expenses, "All Expenses")

    def filter_by_category(self, category):
        """
        Filters the stored expenses to find matches for a specific category.
        
        This function searches through the expense list and extracts only the items 
        that match the user's requested category.
        Python Feature Highlight: This utilizes 'List Comprehension', a highly optimized 
        and readable Python feature that condenses a traditional for-loop and if-statement 
        into a single line of code.
        """
        # Iterate over self.expenses and keep only the items where the category matches (case-insensitive).
        filtered = [exp for exp in self.expenses if exp["category"].lower() == category.lower()]
        # Pass the newly created filtered list to the helper method for printing.
        self._print_expenses(filtered, f"Category: {category}")

    def filter_by_date_range(self, start_date_str, end_date_str):
        """
        Filters the stored expenses to find items within a specific time frame.
        
        This function converts the user's start and end date strings into datetime objects, 
        and then checks each expense to see if its date falls between them.
        Python Feature Highlight: Python allows for direct mathematical comparison of 
        date objects (start <= date <= end), which reads exactly like standard English.
        """
        # Start a try block to handle potential invalid date string inputs.
        try:
            # Convert the start date string into a Python date object.
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
            # Convert the end date string into a Python date object.
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
            
            # Use list comprehension to find all expenses where the date is between the start and end dates.
            filtered = [exp for exp in self.expenses if start_date <= exp["date"] <= end_date]
            # Print the filtered list with a title indicating the date range.
            self._print_expenses(filtered, f"From {start_date_str} to {end_date_str}")
        # Catch any errors that occur during the date string conversion.
        except ValueError:
            # Inform the user of the correct date format.
            print(" x x x Error: Invalid date format. Use YYYY-MM-DD.")

    def get_summary(self):
        """
        Calculates and displays the total expenses overall and per category.
        
        This function iterates through all expenses to sum up the total spent.
        Simultaneously, it dynamically builds a dictionary to track the running 
        total for each individual category.
        """
        # Initialize a float variable to hold the grand total of all expenses.
        total_overall = 0.0
        # Initialize an empty dictionary to map each category to its total spending.
        category_totals = {} 

        # Loop through each expense dictionary in the main list.
        for exp in self.expenses:
            # Extract the numerical amount from the current expense.
            amt = exp["amount"]
            # Extract the category string from the current expense.
            cat = exp["category"]
            # Add the current amount to the grand total.
            total_overall += amt
            # Retrieve the current total for the category (defaulting to 0.0 if new), add the new amount, and update the dict.
            category_totals[cat] = category_totals.get(cat, 0.0) + amt

        # Print a header for the summary section.
        print("\n--- Expense Summary ---")
        # Print the grand total, formatted to two decimal places.
        print(f"Total Expenses: ${total_overall:.2f}")
        # Loop through the key-value pairs in the category_totals dictionary.
        for cat, total in category_totals.items():
            # Print each category and its specific total amount.
            print(f" - {cat}: ${total:.2f}")
        # Print a footer line for the summary section.
        print("--------------------------\n")

    def _print_expenses(self, expense_list, title):
        """
        Helper method to format and print a list of expenses as a table.
        
        This private method handles the visual output of the application. It takes 
        any list of expenses (filtered or unfiltered) and prints them in a neat, 
        aligned table format.
        """
        # Print the title of the table, flanked by hyphens.
        print(f"\n--- {title} ---")
        # Check if the provided list is empty.
        if not expense_list:
            # Print a message if there is no data to display.
            print("No expenses found.")
        # If the list is not empty, proceed to print the table.
        else:
            # Print the table headers, using f-string formatting to set specific column widths (<12 means left-aligned, 12 chars wide).
            print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
            # Print a separator line of 65 hyphens.
            print("-" * 65)
            # Iterate through each expense dictionary in the list.
            for exp in expense_list:
                # Format the date back to a string, and print the row with the same column widths.
                print(f"{exp['date'].strftime('%Y-%m-%d'):<12} | {exp['category']:<15} | ${exp['amount']:<9.2f} | {exp['description']}")
        # Print a final separator line and a newline character for spacing.
        print("-" * 65 + "\n")

def main():
    """
    The main driver function that runs the interactive Command Line Interface.
    
    This function sets up the tracker, populates it with some sample data, 
    and then enters an infinite loop waiting for user input until the user 
    chooses to exit.
    """
    # Create an instance of the ExpenseTracker class.
    tracker = ExpenseTracker()
    
    # Add a sample expense to the tracker.
    tracker.add_expense("2023-10-01", 12.50, "Food", "Lunch at cafe")
    # Add a second sample expense to the tracker.
    tracker.add_expense("2023-10-02", 45.00, "Transport", "Gasoline")
    # Add a third sample expense to the tracker.
    tracker.add_expense("2023-10-05", 150.00, "Shopping", "New shoes")
    # Add a fourth sample expense to the tracker.
    tracker.add_expense("2023-10-10", 25.00, "Food", "Groceries")

    # Start an infinite loop to keep the program running for user interaction.
    while True:
        # Print the main menu options to the console.
        print("\n1. View All | 2. Add Expense | 3. Filter Category | 4. Filter Date | 5. Summary | 6. Exit")
        # Capture the user's input as a string.
        choice = input("Enter choice: ")

        # Check if the user selected option 1.
        if choice == '1':
            # Call the method to display all expenses.
            tracker.view_all()
        # Check if the user selected option 2.
        elif choice == '2':
            # Prompt the user to enter the date.
            date = input("Date (YYYY-MM-DD): ").strip()
            # Prompt the user to enter the dollar amount.
            amt = input("Amount: ").strip()
            # Prompt the user to enter the category name.
            cat = input("Category: ").strip()
            # Prompt the user to enter a brief description.
            desc = input("Description: ").strip()
            # Call the method to add the expense using the collected inputs.
            tracker.add_expense(date, amt, cat, desc)
        # Check if the user selected option 3.
        elif choice == '3':
            # Prompt the user to enter the category they want to filter by.
            cat = input("Enter category to filter: ")
            # Call the method to display expenses matching that category.
            tracker.filter_by_category(cat)
        # Check if the user selected option 4.
        elif choice == '4':
            # Prompt the user to enter the start date for the filter.
            start = input("Start Date (YYYY-MM-DD): ")
            # Prompt the user to enter the end date for the filter.
            end = input("End Date (YYYY-MM-DD): ")
            # Call the method to display expenses within that date range.
            tracker.filter_by_date_range(start, end)
        # Check if the user selected option 5.
        elif choice == '5':
            # Call the method to display the financial summary.
            tracker.get_summary()
        # Check if the user selected option 6.
        elif choice == '6':
            # Print a goodbye message.
            print("Exiting...")
            # Break the while loop, which will terminate the program.
            break
        # Handle the case where the user enters an invalid number or letter.
        else:
            # Print an error message and loop back to the menu.
            print("Invalid choice.")

# This Python idiom ensures that main() is only called if this script is run directly.
# It prevents the program from running automatically if this file is imported as a module elsewhere.
if __name__ == "__main__":
    # Call the main function to start the application.
    main()