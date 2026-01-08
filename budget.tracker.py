print("Welcome to Budget Tracker")

income = int(input("Enter your income: "))

rent = int(input("Enter rent expense: "))
food = int(input("Enter food expense: "))
transport = int(input("Enter transport expense: "))

total_expenses = rent + food + transport
remaining = income - total_expenses

print("Total expenses:", total_expenses)
print("Remaining balance:", remaining)

if remaining < 0:
    print("⚠️ You are over budget!")
else:
    print("✅ You are within budget.")
