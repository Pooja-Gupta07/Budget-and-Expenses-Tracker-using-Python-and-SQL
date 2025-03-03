import db_connection
import user_auth
import income
import expenses
import budget
import reports

def main():
    print("\n💰 Welcome to Budget & Expense Tracker 💰\n")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            user_auth.register_user(username, password)
        
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = user_auth.login_user(username, password)
            
            if user_id:
                print(f"\nWelcome, {username}! 🎉")
                user_dashboard(user_id)
            else:
                print("Invalid login. Please try again.")
        
        elif choice == "3":
            print("Goodbye! 👋")
            break
        
        else:
            print("Invalid choice. Please try again.")

def user_dashboard(user_id):
    while True:
        print("\n📌 User Dashboard")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Set Budget")
        print("5. Check Budget")
        print("6. Generate Report")
        print("7. Logout")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            date = input("Enter date (YYYY-MM-DD): ")
            income.add_income(user_id, amount, source, date)

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            expenses.add_expense(user_id, category, amount, description, date)

        elif choice == "3":
            records = expenses.get_expenses(user_id)
            for rec in records:
                print(f"Category: {rec[0]}, Amount: {rec[1]}, Date: {rec[2]}")

        elif choice == "4":
            category = input("Enter category: ")
            limit_amount = float(input("Enter budget limit: "))
            budget.set_budget(user_id, category, limit_amount)

        elif choice == "5":
            category = input("Enter category to check budget: ")
            budget.check_budget(user_id, category)

        elif choice == "6":
            reports.generate_report(user_id)

        elif choice == "7":
            print("Logging out... 🔐")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
