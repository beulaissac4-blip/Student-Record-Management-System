
import csv
import os

FILE_NAME = "students.csv"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Please enter numbers only!")
        return

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Roll Number", "Name", "Marks"])

        writer.writerow([roll, name, marks])

    print("Student added successfully!")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!")
        return

    with open(FILE_NAME, "r", newline="") as file:
        for row in csv.reader(file):
            print(row)


def update_student():
    roll = input("Enter Roll Number to update: ")
    students = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        students = list(csv.reader(file))

    for row in students[1:]:
        if row[0] == roll:
            row[1] = input("Enter New Name: ")
            row[2] = input("Enter New Marks: ")
            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            csv.writer(file).writerows(students)
        print("Student updated successfully!")
    else:
        print("Student not found!")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    students = []

    with open(FILE_NAME, "r", newline="") as file:
        students = list(csv.reader(file))

    updated = [students[0]]
    found = False

    for row in students[1:]:
        if row[0] == roll:
            found = True
        else:
            updated.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            csv.writer(file).writerows(updated)
        print("Student deleted successfully!")
    else:
        print("Student not found!")


print("\n1. Add Student")
print("2. View Students")
print("3. Update Student")
print("4. Delete Student")

choice = input("Enter your choice: ")

if choice == "1":
    add_student()
elif choice == "2":
    view_students()
elif choice == "3":
    update_student()
elif choice == "4":
    delete_student()
else:
    print("Invalid choice!")
