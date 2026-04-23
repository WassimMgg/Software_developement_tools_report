import csv
import os

# Configuration
DB_FILE = "results.csv"
results_table = []

def calculate(num1, num2, operation):
    """Core logic for arithmetic operations."""
    operations = {
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "*": lambda: num1 * num2,
        "/": lambda: num1 / num2 if num2 != 0 else "Error: Division by zero"
    }
    return operations.get(operation, lambda: "Invalid operation")()

def load_from_csv():
    """Load existing history if the file exists."""
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert strings back to floats where appropriate
                    results_table.append({
                        "num1": float(row["num1"]),
                        "num2": float(row["num2"]),
                        "operation": row["operation"],
                        "result": row["result"]
                    })
            print(f"📊 Loaded {len(results_table)} entries from history.")
        except Exception as e:
            print(f"⚠️ Could not load history: {e}")

def show_history():
    """Displays history in a clean, formatted table."""
    if not results_table:
        print("\n📭 No history found.")
        return
    
    print("\n" + "="*50)
    print(f"{'ID':<4} | {'Expression':<20} | {'Result':<15}")
    print("-" * 50)
    
    for i, row in enumerate(results_table, 1):
        expr = f"{row['num1']} {row['operation']} {row['num2']}"
        print(f"{i:<4} | {expr:<20} | {row['result']:<15}")
    print("="*50)

def save_to_csv():
    """Saves current session to the CSV file."""
    try:
        with open(DB_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["num1", "operation", "num2", "result"])
            writer.writeheader()
            writer.writerows(results_table)
        print("✅ Results saved successfully.")
    except IOError:
        print("❌ Error: Could not write to file.")

def search_history():
    """Search history with case-insensitive keyword matching."""
    keyword = input("🔍 Search (number or operator): ").strip().lower()
    matches = [
        row for row in results_table 
        if keyword in str(row['num1']) or keyword in str(row['num2']) or keyword == row['operation']
    ]
    
    if matches:
        print(f"\n🎯 Found {len(matches)} results:")
        for row in matches:
            print(f"   {row['num1']} {row['operation']} {row['num2']} = {row['result']}")
    else:
        print("Empty-handed! No matching results.")

def clear_history():
    """Wipes the list and offers to delete the physical file."""
    results_table.clear()
    confirm = input("Clear file storage too? (y/n): ").lower()
    if confirm == 'y' and os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    print("🗑️ History cleared.")

# --- Main Interface ---
def main():
    load_from_csv()
    
    while True:
        print("\n🚀 CALCULATOR PRO")
        print("1. New Calculation | 2. Show History | 3. Search")
        print("4. Save to Disk    | 5. Clear All    | 6. Exit")

        choice = input("\nAction > ")

        if choice == "1":
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
                op = input("Operation (+, -, *, /): ").strip()
                
                res = calculate(n1, n2, op)
                print(f"✨ Result: {res}")
                
                results_table.append({"num1": n1, "num2": n2, "operation": op, "result": res})
            except ValueError:
                print("❌ Input Error: Please provide valid numbers.")

        elif choice == "2": show_history()
        elif choice == "3": search_history()
        elif choice == "4": save_to_csv()
        elif choice == "5": clear_history()
        elif choice == "6":
            print("👋 Session ended.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()