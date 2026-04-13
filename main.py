# Simple Calculator with history table

results_table = []  # this will store all results

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    # store in table (as a dictionary)
    results_table.append({
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result
    })

    print("Result:", result)

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        break

# print the table
print("\n📊 Results Table:")
for i, row in enumerate(results_table, start=1):
    print(f"{i}. {row['num1']} {row['operation']} {row['num2']} = {row['result']}")