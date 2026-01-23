/**
 * PROJECT: Expense Tracker Application
 * AUTHOR: Senior C++ Software Engineer / Mentor
 * DESCRIPTION: A console-based application for tracking daily expenses.
 * FEATURES: Add, View, Search, Filter, and Summarize expenses with file persistence.
 */

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <map>
#include <algorithm>
#include <ctime>

using namespace std;

// ============================================================================
// UTILITY TOOLS
// ============================================================================
class Utils {
public:
    static bool isValidDate(const string& date) {
        if (date.length() != 10) return false;
        if (date[4] != '-' || date[7] != '-') return false;

        try {
            int year = stoi(date.substr(0, 4));
            int month = stoi(date.substr(5, 2));
            int day = stoi(date.substr(8, 2));

            if (month < 1 || month > 12) return false;
            if (day < 1 || day > 31) return false;
            if (year < 1900 || year > 2100) return false;
            return true;
        } catch (...) {
            return false;
        }
    }

    static string formatCurrency(double amount) {
        stringstream ss;
        ss << fixed << setprecision(2) << amount;
        return ss.str();
    }
};

// ============================================================================
// DATA MODELS
// ============================================================================
struct Expense {
    string date;        // YYYY-MM-DD
    double amount;
    string category;
    string description;

    // Serialize to string for file storage
    string serialize() const {
        return date + "," + to_string(amount) + "," + category + "," + description;
    }

    // Deserialize from file line
    static Expense deserialize(const string& line) {
        stringstream ss(line);
        string date, amtStr, cat, desc;
        getline(ss, date, ',');
        getline(ss, amtStr, ',');
        getline(ss, cat, ',');
        getline(ss, desc, ',');
        return {date, stod(amtStr), cat, desc};
    }
};

// ============================================================================
// CORE LOGIC MANAGER
// ============================================================================
class ExpenseManager {
private:
    vector<Expense> expenses;
    const string filename = "expenses.txt";

    void loadFromFile() {
        ifstream file(filename);
        if (!file.is_open()) return;
        
        expenses.clear();
        string line;
        while (getline(file, line)) {
            if (!line.empty()) {
                expenses.push_back(Expense::deserialize(line));
            }
        }
        file.close();
    }

    void saveToFile() {
        ofstream file(filename);
        for (const auto& e : expenses) {
            file << e.serialize() << endl;
        }
        file.close();
    }

public:
    ExpenseManager() {
        loadFromFile();
    }

    void addExpense(const Expense& e) {
        expenses.push_back(e);
        saveToFile();
        cout << "\n[Success] Expense added successfully!\n";
    }

    void displayAll() const {
        if (expenses.empty()) {
            cout << "\nNo expenses recorded yet.\n";
            return;
        }
        printTable(expenses);
    }

    void filterByCategory(const string& category) const {
        vector<Expense> filtered;
        for (const auto& e : expenses) {
            if (e.category == category) filtered.push_back(e);
        }
        if (filtered.empty()) cout << "\nNo results found for category: " << category << endl;
        else printTable(filtered);
    }

    void filterByDateRange(const string& start, const string& end) const {
        vector<Expense> filtered;
        for (const auto& e : expenses) {
            if (e.date >= start && e.date <= end) filtered.push_back(e);
        }
        if (filtered.empty()) cout << "\nNo results found in that date range.\n";
        else printTable(filtered);
    }

    void searchByDescription(const string& query) const {
        vector<Expense> filtered;
        string lowerQuery = query;
        transform(lowerQuery.begin(), lowerQuery.end(), lowerQuery.begin(), ::tolower);

        for (const auto& e : expenses) {
            string lowerDesc = e.description;
            transform(lowerDesc.begin(), lowerDesc.end(), lowerDesc.begin(), ::tolower);
            if (lowerDesc.find(lowerQuery) != string::npos) {
                filtered.push_back(e);
            }
        }
        if (filtered.empty()) cout << "\nNo results matching: " << query << endl;
        else printTable(filtered);
    }

    void showSummary() const {
        if (expenses.empty()) {
            cout << "\nNo data to summarize.\n";
            return;
        }

        double total = 0;
        map<string, double> categoryTotals;

        for (const auto& e : expenses) {
            total += e.amount;
            categoryTotals[e.category] += e.amount;
        }

        cout << "\n========================================";
        cout << "\n        EXPENSE SUMMARY REPORT        ";
        cout << "\n========================================";
        cout << "\nTotal Expenses: $" << Utils::formatCurrency(total);
        cout << "\n\nBreakdown by Category:";
        for (auto const& [cat, amt] : categoryTotals) {
            cout << "\n- " << left << setw(15) << cat << ": $" << Utils::formatCurrency(amt);
        }
        cout << "\n========================================\n";
    }

    void printTable(const vector<Expense>& data) const {
        cout << "\n" << setfill('-') << setw(75) << "-" << setfill(' ') << endl;
        cout << left << setw(12) << "Date" 
             << setw(10) << "Amount" 
             << setw(15) << "Category" 
             << "Description" << endl;
        cout << setfill('-') << setw(75) << "-" << setfill(' ') << endl;

        for (const auto& e : data) {
            cout << left << setw(12) << e.date 
                 << "$" << setw(9) << Utils::formatCurrency(e.amount)
                 << setw(15) << e.category 
                 << e.description << endl;
        }
        cout << setfill('-') << setw(75) << "-" << setfill(' ') << endl;
    }
};

// ============================================================================
// USER INTERFACE (CONSOLE)
// ============================================================================
void displayMenu() {
    cout << "\n--- EXPENSE TRACKER PRO v1.0 ---";
    cout << "\n1. Add Expense";
    cout << "\n2. View All Expenses";
    cout << "\n3. Filter by Category";
    cout << "\n4. Filter by Date Range";
    cout << "\n5. Search Description";
    cout << "\n6. View Summary Reports";
    cout << "\n0. Exit";
    cout << "\nSelect an option: ";
}

int main() {
    ExpenseManager manager;
    int choice;

    do {
        displayMenu();
        if (!(cin >> choice)) {
            cin.clear();
            cin.ignore(1000, '\n');
            continue;
        }

        switch (choice) {
            case 1: {
                string d, c, desc;
                double a;
                cout << "Enter Date (YYYY-MM-DD): "; cin >> d;
                while (!Utils::isValidDate(d)) {
                    cout << "Invalid format. Re-enter Date (YYYY-MM-DD): "; cin >> d;
                }
                cout << "Enter Amount: "; cin >> a;
                cout << "Enter Category (e.g., Food, Transport, Rent): "; cin >> c;
                cin.ignore();
                cout << "Enter Description: "; getline(cin, desc);
                manager.addExpense({d, a, c, desc});
                break;
            }
            case 2:
                manager.displayAll();
                break;
            case 3: {
                string cat;
                cout << "Enter Category to filter: "; cin >> cat;
                manager.filterByCategory(cat);
                break;
            }
            case 4: {
                string start, end;
                cout << "Enter Start Date (YYYY-MM-DD): "; cin >> start;
                cout << "Enter End Date (YYYY-MM-DD): "; cin >> end;
                manager.filterByDateRange(start, end);
                break;
            }
            case 5: {
                string query;
                cout << "Enter search keyword: "; cin >> query;
                manager.searchByDescription(query);
                break;
            }
            case 6:
                manager.showSummary();
                break;
            case 0:
                cout << "Exiting. Data saved to file.\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 0);

    return 0;
}
