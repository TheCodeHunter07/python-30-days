# Build a menu-driven student records system. Each student is a dictionary with a roll number, name, and marks
# for 3 subjects.
# REQUIREMENTS
# • Add a student — reject duplicate roll numbers
# • View all students in a table
# • Search by roll number or name
# • Update marks; delete a student
# • Show the class topper and class average
# • Invalid menu input must never crash the program

students = [
    {
        "roll_number": 101,
        "name": "Rahul",
        "marks": {
            "maths": 85,
            "science": 90,
            "english": 78
        }
    },
    {
        "roll_number": 102,
        "name": "Priya",
        "marks": {
            "maths": 92,
            "science": 88,
            "english": 95
        }
    },
    {
        "roll_number": 103,
        "name": "Aarav",
        "marks": {
            "maths": 76,
            "science": 82,
            "english": 80
        }
    }
]


# • Add a student — reject duplicate roll numbers

while True:

    print("=" * 32)
    print("          STUDENT RECORDS MANAGER")
    print("=" * 32)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Show Class Topper")
    print("7. Show Class Average")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":

        print("\n--- Add New Student ---")

        name = input("Enter student name: ")
        roll_no = int(input("Enter student roll number: "))

        duplicate = False

        for student in students:
            if student["roll_number"] == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Error: Roll number already exists!")

        else:

            maths = int(input("Enter Maths marks: "))
            science = int(input("Enter Science marks: "))
            english = int(input("Enter English marks: "))

            marks = {
                "maths": maths,
                "science": science,
                "english": english
            }

            new_student = {
                "roll_number": roll_no,
                "name": name,
                "marks": marks
            }

            students.append(new_student)

            print("Student record added successfully!")

    # VIEW ALL STUDENTS
    elif choice == "2":

        print("\n--- View All Students ---")

        print("-" * 60)

        print(f"{'Name':<15} {'Roll No.':<12} {'Maths':>8} {'Science':>8} {'English':>8}")

        print("-" * 60)

        for student in students:

            print(
                f"{student['name']:<15} "
                f"{student['roll_number']:<12} "
                f"{student['marks']['maths']:>8} "
                f"{student['marks']['science']:>8} "
                f"{student['marks']['english']:>8}"
                 )

        print("-" * 60)

    # Search by roll number or name
    
    elif choice == "3":

        print("\n--- Search Student ---")
        print("1. Search by Roll Number")
        print("2. Search by Name")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":

            roll_no = int(input("Enter roll number to search: "))
            found = False

            for student in students:

                if roll_no == student["roll_number"]:
                    found = True
                    print(
                        f"{student['name']:<15} "
                        f"{student['roll_number']:<12} "
                        f"{student['marks']['maths']:>8} "
                        f"{student['marks']['science']:>8} "
                        f"{student['marks']['english']:>8}"
                    )

            if not found:
                print("Student record not found!")

        elif search_choice == "2":

            name = input("Enter name to search: ")
            found = False

            for student in students:

                if name.lower() == student["name"].lower():
                    found = True

                    
                    print(
                        f"{student['name']:<15} "
                        f"{student['roll_number']:<12} "
                        f"{student['marks']['maths']:>8} "
                        f"{student['marks']['science']:>8} "
                        f"{student['marks']['english']:>8}"
                    )

            if not found:
                print("Student record not found!")

        else:
            print("Invalid search choice!")

    # Update marks

    elif choice == "4":

        print("\n--- Update Student Marks ---")

        roll_no = int(input("Enter student roll number: "))

        found = False

        for student in students:

            if student["roll_number"] == roll_no:

                found = True

                print(f"Student Name: {student['name']}")
                print("Current Marks:", student["marks"])

                print("\nSelect Subject:")
                print("1. Maths")
                print("2. Science")
                print("3. English")

                subject_choice = input("Enter your subject choice: ")

                if subject_choice == "1":

                    maths = int(input("Enter the new maths marks: "))
                    student["marks"]["maths"] = maths

                    print("Maths marks updated successfully!")

                elif subject_choice == "2":

                    science = int(input("Enter the new science marks: "))
                    student["marks"]["science"] = science

                    print("Science marks updated successfully!")

                elif subject_choice == "3":

                    english = int(input("Enter the new english marks: "))
                    student["marks"]["english"] = english

                    print("English marks updated successfully!")

                else:
                    print("Invalid subject choice!")

                break

        if not found:
            print("Student record not found!")


    elif choice == "5":

        print("\n--- Delete Student ---")

        roll_no = int(input("Enter student roll number to delete: "))

        found = False

        for student in students:

            if student["roll_number"] == roll_no:

                found = True

                students.remove(student)

                print("Student deleted successfully!")
                break

        if not found:
            print("Student record not found!")

    # SHOW CLASS TOPPER

    elif choice == "6":

        print("\n--- Class Topper ---")

        highest_marks = 0
        topper = None

        for student in students:

            # 1. Calculate total marks
            total = student["marks"]["maths"] + student["marks"]["science"] + student["marks"]["english"]

            # 2. Check if current student's total is higher
            if total > highest_marks:

                highest_marks = total
                topper = student

        # 3. Display topper details
        if topper is not None:

            print("Class Topper:", topper["name"])
            print("Roll Number:", topper["roll_number"])
            print("Total Marks:", highest_marks)


    # Show Class Average

    elif choice == "7":

        print("\n--- Class Average ---")

        total_marks = 0

        for student in students:

            student_total = (
                student["marks"]["maths"]
                + student["marks"]["science"]
                + student["marks"]["english"]
            )

            total_marks += student_total

        if len(students) > 0:
            class_average = total_marks / (len(students) * 3)
            print(f"Class Average: {class_average:.2f}")
        else:
            print("No student records available.")
           

    # EXIT
    elif choice == "8":

        print("Exiting Student Records Manager...")
        break

    else:
        print("Invalid choice! Please try again.")
   
           