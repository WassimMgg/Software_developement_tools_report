import csv

results_table = []

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

def show_history():
    if not results_table:
        print("No history yet.")
        return
    print("\n📊 History:")
    for i, row in enumerate(results_table, 1):
        print(f"{i}. {row['num1']} {row['operation']} {row['num2']} = {row['result']}")

def save_to_csv():
    with open("results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["num1", "operation", "num2", "result"])
        writer.writeheader()
        writer.writerows(results_table)
    print("✅ Results saved to results.csv")

def search_history():
    keyword = input("Enter number or operation to search: ")
    found = False
    for row in results_table:
        if keyword in str(row.values()):
            print(f"{row['num1']} {row['operation']} {row['num2']} = {row['result']}")
            found = True
    if not found:
        print("No matching results.")

def clear_history():
    results_table.clear()
    print("🗑️ History cleared.")

# Main loop
while True:
    print("\n==== Calculator Menu ====")
    print("1. New Calculation")
    print("2. Show History")
    print("3. Save to CSV")
    print("4. Search History")
    print("5. Clear History")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            result = calculate(num1, num2, operation)

            results_table.append({
                "num1": num1,
                "num2": num2,
                "operation": operation,
                "result": result
            })

            print("Result:", result)

        except ValueError:
            print("❌ Invalid input. Please enter numbers.")

    elif choice == "2":
        show_history()

    elif choice == "3":
        save_to_csv()

    elif choice == "4":
        search_history()

    elif choice == "5":
        clear_history()

    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
        print("Please choose a valid option from the menu.") 