from datetime import datetime
expenses = []


def add_expense():
    item = input("Enter item name: ")
    amount = input("Enter amount spent:  ")

    try:
        amount = float(amount)
    except ValueError:
        print(" Invalid amount. Please enter a number.\n")
        return

    date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"date": date, "item": item, "amount": amount})
    print(" Expense added!\n")


def view_total():
    today = datetime.now().strftime("%Y-%m-%d")
    total = sum(exp["amount"] for exp in expenses if exp["date"] == today)
    print(f"Total expenses today ({today}): ₹{total:.2f}\n")


def view_all():
    if not expenses:
        print(" No expenses to show.\n")
        return

    print("All Entries:")
    for exp in expenses:
        print(f"{exp['date']} - {exp['item']}: ₹{exp['amount']}")
    print()


def main():
    while True:
        print(" Welcome to Expense Tracker ")
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View All Entries")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            view_all()
        elif choice == "4":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1–4.\n")

if __name__ == "__main__":
    main()
