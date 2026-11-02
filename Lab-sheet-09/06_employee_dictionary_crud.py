# Add, view, update, and delete employee entries in a dictionary.
employees = {1: {"name": "Mina", "department": "Sales"}, 2: {"name": "Arun", "department": "IT"}}
while True:
    print("\n1 Add  2 View  3 Update  4 Delete  5 Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            emp_id = int(input("Employee ID: "))
            if emp_id in employees:
                print("ID already exists.")
            else:
                employees[emp_id] = {"name": input("Name: ").strip(), "department": input("Department: ").strip()}
                print("Employee added.")
        elif choice == "2":
            print(employees if employees else "No employees.")
        elif choice == "3":
            emp_id = int(input("Employee ID: "))
            if emp_id in employees:
                employees[emp_id] = {"name": input("New name: ").strip(), "department": input("New department: ").strip()}
                print("Employee updated.")
            else:
                print("Employee not found.")
        elif choice == "4":
            emp_id = int(input("Employee ID: "))
            print("Employee deleted." if employees.pop(emp_id, None) else "Employee not found.")
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")
    except ValueError:
        print("Employee ID must be a number.")
