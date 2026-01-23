Expense Tracker Application (C++)

A robust, console-based personal finance management tool designed to help users track, categorize, and analyze their spending habits. This project demonstrates high-level C++ programming concepts including Object-Oriented Design, file I/O, and the use of the Standard Template Library (STL).

🚀 Features

Persistent Storage: Expenses are automatically saved to and loaded from a local text file (expenses.txt).

Full CRUD Operations: Add new expenses with date, amount, category, and description.

Advanced Filtering:

Filter by specific categories (e.g., Food, Travel).

Filter by custom date ranges (YYYY-MM-DD).

Search Functionality: Keyword search across expense descriptions.

Financial Analytics:

Real-time calculation of total expenditures.

Automatic grouping and sub-totaling by category.

Data Validation: Strict date format checking and numeric amount verification.

📂 Folder Structure

expense-tracker/
├── main.cpp          # Unified source code (Main, Logic, Models)
├── expenses.txt      # Data file (Auto-generated on first run)
├── README.md         # Project documentation
└── instructions.md   # Compilation and setup guide


🧠 System Architecture

Main Classes & Components

Expense (Struct): The data model containing attributes for date, amount, category, and description. It includes methods for serialization to store data in a flat-file format.

ExpenseManager (Class): The heart of the application. It handles the vector of expenses, performs all filtering logic, and manages the stream-based file operations.

Utils (Static Class): Contains helper functions for date validation using substring parsing and currency formatting using string streams.

Logic Flow

Initialization: On startup, ExpenseManager reads expenses.txt and populates an internal std::vector<Expense>.

User Interaction: A do-while loop in main() captures user input via a numbered menu.

Processing: Depending on the selection, the manager either appends to the vector (Save) or iterates through it with conditional logic (Filter/Search).

Finalization: Any change to the list triggers an automatic saveToFile() call to ensure data integrity before the program terminates.

🛠️ Setup and Installation

To compile this project, ensure you have a C++17 compatible compiler.

# Compile
g++ -std=c++17 main.cpp -o ExpenseTracker

# Run
./ExpenseTracker


For detailed instructions on Windows or macOS, please refer to instructions.md.

📖 Usage Examples

Action

Input Example

Add Expense

2023-12-01, 1200.00, Rent, Monthly Apartment Rent

Filter Date

2023-01-01 to 2023-12-31

Search

Pizza (Returns all descriptions containing "pizza")

📸 Sample Screenshots

(Placeholders - In a real GitHub repo, you would upload images here)

[Screenshot: Main Menu Interface]

[Screenshot: Expense Summary Table]

[Screenshot: Category-wise Breakdown]

⚠️ Limitations

Console Only: No Graphical User Interface (GUI).

Single User: Designed for a single user/local file access.

Simple Validation: Does not account for leap years in the simplified date validation logic.

🔮 Future Improvements

[ ] Implement a GUI using Qt or wxWidgets.

[ ] Add the ability to export reports to CSV or PDF format.

[ ] Integrate a database (SQLite) for handling larger datasets.

[ ] Add password protection/encryption for stored data.

Author: [Your Name/GitHub Profile]

Academic Mentor: Senior C++ Engineer Lead
