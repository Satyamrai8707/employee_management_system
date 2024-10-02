import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "satyamrai",
    database = "employee_management_system"
)



cursor = connection.cursor()

def add_employee(empID, name, age, department, salary):
    query = "insert into employee(EmployeeID, name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"
    values = (empID, name, age, department, salary)
    cursor.execute(query, values)
    mydb.commit()
    print("Employees added successfully")

def display_employees():
    query = "select * from employee"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}, Salary: {row[4]}")

def delete_employee(emp_id):
    query = "delete from employee WHERE employeeid = %s"
    cursor.execute(query, (emp_id,))
    mydb.commit()
    print("Employee deleted successfully!")

def update_employee(emp_id, name=None, age=None, department=None, salary=None):
    updates = []
    values = []
    if name:
        updates.append("name = %s")
        values.append(name)
    if age:
        updates.append("age = %s")
        values.append(age)
    if department:
        updates.append("department = %s")
        values.append(department)
    if salary:
        updates.append("salary = %s")
        values.append(salary)

    query = f"update employee SET {', '.join(updates)} WHERE employeeid = %s"
    values.append(emp_id)
    cursor.execute(query, values)
    mydb.commit()
    print("Employee updated successfully!")


def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Display Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID :")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            add_employee(emp_id, name, age, department, salary)

        elif choice == '2':
            emp_id = input("Enter employee ID to update: ")
            name = input("Enter name (or leave blank): ") or None
            age = input("Enter age (or leave blank): ") or None
            department = input("Enter department (or leave blank): ") or None
            salary = input("Enter salary (or leave blank): ") or None
            age = int(age) if age else None
            salary = float(salary) if salary else None
            update_employee(emp_id, name, age, department, salary)

        elif choice == '3':
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(emp_id)

        elif choice == '4':
            display_employees()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

menu()
