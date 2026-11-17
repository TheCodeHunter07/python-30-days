# ASSIGNMENT
# Stretch: Add full error handling to your Stage 2 Student Records Manager.

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

        try:
            name = input("Enter student name: ")
            roll_no = int(input("Enter student roll number: "))

        except ValueError:
            print("Enter a valid integer for roll number!")
            continue

        duplicate = False

        for student in students:

            if student["roll_number"] == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Error: Roll number already exists!")

        else:

            try:
                maths = int(input("Enter Maths marks out of 100: "))
                science = int(input("Enter Science marks out of 100: "))
                english = int(input("Enter English marks out of 100: "))

            except ValueError:
                print("Enter integer marks!")
                continue

            if maths < 0 or maths > 100 or science < 0 or science > 100 or english < 0 or english > 100:
                print("Marks must be between 0 and 100!")
                continue

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

        if len(students) == 0:
            print("No student records available!")

        else:

            print("-" * 60)

            print(f"{'Name':<15} {'Roll No.':<12} {'Maths':>8} {'Science':>8} {'English':>8}")

            print("-" * 60)

            for student in students:

                try:
                    print(
                        f"{student['name']:<15} "
                        f"{student['roll_number']:<12} "
                        f"{student['marks']['maths']:>8} "
                        f"{student['marks']['science']:>8} "
                        f"{student['marks']['english']:>8}"
                    )

                except KeyError as e:
                    print("Missing student information:", e)

            print("-" * 60)


    # SEARCH STUDENT

    elif choice == "3":

        print("\n--- Search Student ---")
        print("1. Search by Roll Number")
        print("2. Search by Name")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":

            try:
                roll_no = int(input("Enter roll number to search: "))

            except ValueError:
                print("Enter a valid integer roll number!")
                continue

            found = False

            for student in students:

                try:

                    if roll_no == student["roll_number"]:

                        found = True

                        print(
                            f"{student['name']:<15} "
                            f"{student['roll_number']:<12} "
                            f"{student['marks']['maths']:>8} "
                            f"{student['marks']['science']:>8} "
                            f"{student['marks']['english']:>8}"
                        )

                except KeyError as e:
                    print("Missing student information:", e)

            if not found:
                print("Student record not found!")


        elif search_choice == "2":

            name = input("Enter name to search: ")

            found = False

            for student in students:

                try:

                    if name.lower() == student["name"].lower():

                        found = True

                        print(
                            f"{student['name']:<15} "
                            f"{student['roll_number']:<12} "
                            f"{student['marks']['maths']:>8} "
                            f"{student['marks']['science']:>8} "
                            f"{student['marks']['english']:>8}"
                        )

                except KeyError as e:
                    print("Missing student information:", e)

            if not found:
                print("Student record not found!")

        else:
            print("Invalid search choice!")


    # UPDATE STUDENT MARKS

    elif choice == "4":

        print("\n--- Update Student Marks ---")

        try:
            roll_no = int(input("Enter student roll number: "))

        except ValueError:
            print("Enter a valid integer roll number!")
            continue

        found = False

        for student in students:

            try:

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

                        try:
                            maths = int(input("Enter the new maths marks: "))

                        except ValueError:
                            print("Enter integer marks!")
                            continue

                        if maths < 0 or maths > 100:
                            print("Marks must be between 0 and 100!")
                            continue

                        student["marks"]["maths"] = maths

                        print("Maths marks updated successfully!")


                    elif subject_choice == "2":

                        try:
                            science = int(input("Enter the new science marks: "))

                        except ValueError:
                            print("Enter integer marks!")
                            continue

                        if science < 0 or science > 100:
                            print("Marks must be between 0 and 100!")
                            continue

                        student["marks"]["science"] = science

                        print("Science marks updated successfully!")


                    elif subject_choice == "3":

                        try:
                            english = int(input("Enter the new english marks: "))

                        except ValueError:
                            print("Enter integer marks!")
                            continue

                        if english < 0 or english > 100:
                            print("Marks must be between 0 and 100!")
                            continue

                        student["marks"]["english"] = english

                        print("English marks updated successfully!")

                    else:
                        print("Invalid subject choice!")

                    break

            except KeyError as e:
                print("Missing student information:", e)

        if not found:
            print("Student record not found!")


    # DELETE STUDENT

    elif choice == "5":

        print("\n--- Delete Student ---")

        try:
            roll_no = int(input("Enter student roll number to delete: "))

        except ValueError:
            print("Enter a valid integer roll number!")
            continue

        found = False

        for student in students:

            try:

                if student["roll_number"] == roll_no:

                    found = True

                    students.remove(student)

                    print("Student deleted successfully!")
                    break

            except KeyError as e:
                print("Missing student information:", e)

        if not found:
            print("Student record not found!")


    # SHOW CLASS TOPPER

    elif choice == "6":

        print("\n--- Class Topper ---")

        highest_marks = -1
        topper = None

        for student in students:

            try:

                total = (
                    student["marks"]["maths"]
                    + student["marks"]["science"]
                    + student["marks"]["english"]
                )

                if total > highest_marks:

                    highest_marks = total
                    topper = student

            except KeyError as e:
                print("Missing student information:", e)

        if topper is not None:

            print("Class Topper:", topper["name"])
            print("Roll Number:", topper["roll_number"])
            print("Total Marks:", highest_marks)

        else:
            print("No valid student records available!")


    # SHOW CLASS AVERAGE

    elif choice == "7":

        print("\n--- Class Average ---")

        total_marks = 0
        valid_students = 0

        for student in students:

            try:

                student_total = (
                    student["marks"]["maths"]
                    + student["marks"]["science"]
                    + student["marks"]["english"]
                )

                total_marks += student_total
                valid_students += 1

            except KeyError as e:
                print("Missing student information:", e)

        if valid_students > 0:

            class_average = total_marks / (valid_students * 3)

            print(f"Class Average: {class_average:.2f}")

        else:
            print("No student records available!")


    # EXIT

    elif choice == "8":

        print("Exiting Student Records Manager...")
        break


    else:
        print("Invalid choice! Please try again.")