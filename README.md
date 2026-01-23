# Expense Tracker Application (C++)

A robust, console-based personal finance management tool designed to help users track, categorize, and analyze their spending habits. This project demonstrates high-level C++ programming concepts including Object-Oriented Design, file I/O, and the use of the Standard Template Library (STL).

---

## Features

* **Persistent Storage:** Expenses are automatically saved to and loaded from a local text file (expenses.txt).

* **Full CRUD Operations:** Add new expenses with date, amount, category, and description.

* **Advanced Filtering:**

  * Filter by specific categories (e.g., Food, Travel).

  * Filter by custom date ranges (YYYY-MM-DD).

* **Search Functionality:** Keyword search across expense descriptions.

* **Financial Analytics:**

  * Real-time calculation of total expenditures.

  * Automatic grouping and sub-totaling by category.

* **Data Validation:** Strict date format checking and numeric amount verification.

---

## Folder Structure

```
  expense-tracker/
  │
  ├── main.cpp          # Unified source code (Main, Logic, Models)
  ├── README.md         # Project documentation (very important)
  ├── .gitignore        # C++ gitignore file
  ├── LICENSE           # MIT License file
  └── expenses.txt      # (Optional) Auto-generated on first run — DO NOT upload
  
```

---

## System Architecture

### Main Classes & Components

* **Expense (Struct):** The data model containing attributes for date, amount, category, and description. It includes methods for serialization to store data in a flat-file format.

* **ExpenseManager (Class):** The heart of the application. It handles the vector of expenses, performs all filtering logic, and manages the stream-based file operations.

* **Utils (Static Class):** Contains helper functions for date validation using substring parsing and currency formatting using string streams.

---

## Logic Flow

* **Initialization:** On startup, ExpenseManager reads expenses.txt and populates an internal std::vector<Expense>.

* **User Interaction:** A do-while loop in main() captures user input via a numbered menu.

* **Processing:** Depending on the selection, the manager either appends to the vector (Save) or iterates through it with conditional logic (Filter/Search).

* **Finalization:** Any change to the list triggers an automatic saveToFile() call to ensure data integrity before the program terminates.

---

## Setup and Installation

To compile this project, ensure you have a C++17 compatible compiler.

### Compile

```
g++ -std=c++17 main.cpp -o ExpenseTracker
```

### Run

```
./ExpenseTracker
```

---

## Detailed Build & Run Instructions (For Grading & Testing)

These instructions are written for instructors and graders who will clone and run this project directly from GitHub.

---

### Step 1: Clone the Repository from GitHub

Open a terminal and run:

```
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd expense-tracker
```

Example:

```
git clone https://github.com/username/expense-tracker.git
cd expense-tracker
```

---

### Step 2: Verify C++ Compiler Installation

Ensure a C++ compiler (g++) is installed.

Check version:

```
g++ --version
```

If not installed:

* **Windows:** Install MinGW or use Visual Studio with C++ workload

* **Linux (Ubuntu/Debian):**

```
sudo apt install g++
```

* **macOS (Xcode Command Line Tools):**

```
xcode-select --install
```

---

### Step 3: Compile the Program

From inside the project folder, run:

```
g++ -std=c++17 main.cpp -o ExpenseTracker
```

This will generate an executable file named:

* ExpenseTracker (Linux / macOS)

* ExpenseTracker.exe (Windows)

---

### Step 4: Run the Program

* **Linux / macOS:**

```
./ExpenseTracker
```

* **Windows (Command Prompt / PowerShell):**

```
ExpenseTracker.exe
```

---

### Step 5: Using the Application

* After running, the main menu will appear

* Enter a number (0–6) to select an option

* Follow on-screen prompts to add, filter, search, or summarize expenses

* On first run:

  * The file expenses.txt will be automatically created

  * All future expenses will be saved and loaded from this file

---

### Step 6: Cleaning & Rebuilding (Optional)

If recompilation is needed:

```
rm ExpenseTracker
g++ -std=c++17 main.cpp -o ExpenseTracker
```

---

### Troubleshooting

* **Command not found: g++**
  Install a C++ compiler (see Step 2)

* **Permission denied (Linux/macOS)**

```
chmod +x ExpenseTracker
./ExpenseTracker
```

* **No expenses showing**
  Ensure expenses.txt is in the same directory as the executable

---

## Usage Examples

* **Add Expense**
  Input Example: 2023-12-01, 1200.00, Rent, Monthly Apartment Rent

* **Filter Date**
  Input Example: 2023-01-01 to 2023-12-31

* **Search**
  Input Example: Pizza (Returns all descriptions containing "pizza")

---

## Limitations

* Console Only: No Graphical User Interface (GUI).

* Single User: Designed for a single user/local file access.

* Simple Validation: Does not account for leap years in the simplified date validation logic.

---

## Future Improvements

* [ ] Implement a GUI using Qt or wxWidgets.

* [ ] Add the ability to export reports to CSV or PDF format.

* [ ] Integrate a database (SQLite) for handling larger datasets.

* [ ] Add password protection/encryption for stored data.

---

## Author & Credits

* Author: [Your Name / GitHub Profile]

* Academic Mentor: Senior C++ Engineer Lead
