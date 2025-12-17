import csv

file_name = "expenses.csv"

# Create file if not exists
try:
    open(file_name, "x").close()
except:
    pass


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    note = input("Enter note: ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, note])

    print("✔ Expense added successfully!\n")


def view_expenses():
    print("\n----- All Expenses -----")
    total = 0

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    amount, category, note = row
                    total += float(amount)
                    print(f"₹{amount} | {category} | {note}")
    except:
        print("No expenses found.")

    print(f"\nTotal Spent: ₹{total}")
    print("------------------------\n")


def filter_by_category():
    category = input("Enter category to filter: ")
    print(f"\n--- Expenses in {category} ---")

    total = 0

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1].lower() == category.lower():
                amount, _, note = row
                total += float(amount)
                print(f"₹{amount} | {note}")

    print(f"Total in {category}: ₹{total}\n")


def menu():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid option. Try again!\n")


menu()
