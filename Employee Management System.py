# Employee records stored as a tuple of tuples (Employee ID, Name, Department)
employees = ((201, "John Doe", "HR"),(202, "Jane Smith", "IT"),(203, "Mike Johnson", "Finance"),)

while True:
    # Display menu options
    print("\n1. Display Employees")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Exit")

    # Get user input for menu selection
    choice = input("Enter your choice: ")

    if choice == "1":  # Display all employees
        print("\nEmployee Records:")
        print("-----------------")
        for employee in employees:
            # Iterate through the tuple and print employee details
            print(f"ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}")
        print("-----------------\n")

    elif choice == "2":  # Search employee by ID
        search_id = input("Enter Employee ID to Search: ")
        if search_id.isdigit():  # Ensure input is numeric
            search_id = int(search_id)
            found = False
            for employee in employees:
                if employee[0] == search_id:  # Match ID with records
                    print(f"\nEmployee Found: ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}\n")
                    found = True
                    break  # Exit loop once found
            if not found:
                print("\nEmployee Not Found!\n")
        else:
            print("\nInvalid Input! Please enter a valid numeric ID.\n")

    elif choice == "3":  # Add a new employee
        emp_id = input("Enter Employee ID: ")
        if emp_id.isdigit():  # Ensure ID is a number
            emp_id = int(emp_id)
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ")

            employees = employees + ((emp_id, name, department),)  # Create a new tuple to store the added employee
            print("\nEmployee Added Successfully!\n")
        else:
            print("\nInvalid Input! Employee ID must be a number.\n")

    elif choice == "4":  # Exit the program
        print("Exiting Program...")
        break  # Terminate the loop

    else:
        print("\nInvalid Choice! Try Again.\n")  # Handle invalid menu inputs
