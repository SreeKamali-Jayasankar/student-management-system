import json

def load_students():
    global students
    try:
        with open("studentsdatabase.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
         

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file , indent = 4)

def get_students_id():
    while True:
        try:
            sid = int(input("Enter student ID: "))
            return str(sid)
        except ValueError:
            print("Invalid input. Please enter a valid student ID.")

def students_exist(sid):
      for student in students:
            if student["id"] == sid:
                  return True 
      return False

students=[]

def add_student():
    sid = get_students_id()
    if students_exist(sid):
        print(f"Student {sid} already exists.")
        return
    
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    
    students.append({"id": sid, "name": name,"age": age,"course": course})
    print(f"Student {sid} : {name} added successfully.")
    save_students()

def delete_student():
    sid = get_students_id()
    if students_exist(sid):
        for student in students:
            if student["id"] == sid:
                students.remove(student)
                print(f"Student {sid} deleted successfully.")
                save_students()
                return
        else:
            print(f"Student {sid} not found.")

def search_student():
    sid = get_students_id()
    for student in students:
        if student["id"] == sid:
            print(f"Student found: {student}")
            return
        else:
            print(f"Student {sid} not found.")

def display_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")

def update_student():
    sid = get_students_id()
    for student in students:
        if student["id"] == sid:
            print(f"Current details: {student}")
            student["name"] = input("Enter new student name: ")
            student["age"] = input("Enter new student age: ")
            student["course"] = input("Enter new student course: ")
            print(f"Student {sid} updated successfully.")
            save_students()
            return
        else:
            print(f"Student {sid} not found.")

while True:
    load_students()
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        delete_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        display_students()
    elif choice == '5':
        update_student()
    elif choice == '6':
        print("Thank you for using the Student Management System. Data saved successfully.")
        break
    else:
        print("Invalid choice. Please try again.")           