
FILE_NAME = "attendance.txt"
students = []


# Load data from file
def load_data():
    global students

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 4:
                student = {
                    "roll": int(data[0]),
                    "name": data[1],
                    "held": int(data[2]),
                    "attended": int(data[3])
                }
                students.append(student)

        file.close()

    except FileNotFoundError:
        students = []


# Save data to file
def save_data():
    file = open(FILE_NAME, "w")

    for student in students:
        file.write(
            str(student["roll"]) + "|" +
            student["name"] + "|" +
            str(student["held"]) + "|" +
            str(student["attended"]) + "\n"
        )

    file.close()


# Add student
def add_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists.")
            return

    name = input("Enter Student Name: ")

    student = {
        "roll": roll,
        "name": name,
        "held": 0,
        "attended": 0
    }

    students.append(student)
    save_data()

    print("Student added:", roll, "|", name,
          "| Held: 0 | Attended: 0")


# Mark attendance
def mark_attendance():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:

            status = input("Enter Status (P/A): ").upper()

            if status == "P":
                student["held"] += 1
                student["attended"] += 1

            elif status == "A":
                student["held"] += 1

            else:
                print("Invalid status. Enter P or A.")
                return

            save_data()
            print("Attendance marked successfully.")
            return

    print("Roll number", roll, "not found.")


# View attendance percentage
def view_percentage():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:

            if student["held"] == 0:
                print(student["name"],
                      "Attendance 0.00% (no classes held yet)")
            else:
                percentage = (
                    student["attended"] / student["held"]
                ) * 100

                print(student["name"],
                      "Attendance {:.2f}%".format(percentage))

            return

    print("Roll number", roll, "not found.")


# Shortage list
def shortage_list():
    for student in students:

        if student["held"] == 0:
            percentage = 0.00
        else:
            percentage = (
                student["attended"] / student["held"]
            ) * 100

        if percentage < 75:
            print("Below 75%:",
                  student["roll"], "|",
                  student["name"], "|",
                  "{:.2f}%".format(percentage))

        else:
            print(student["name"],
                  "({:.2f}%) meets the requirement.".format(percentage))


# Main menu
def main():
    load_data()

    while True:
        print("\n===== STUDENT ATTENDANCE MANAGER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Percentage")
        print("4. Shortage List")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            view_percentage()

        elif choice == "4":
            shortage_list()

        elif choice == "5":
            save_data()
            print("Exiting Student Attendance Manager.")
            break

        else:
            print("Invalid choice. Enter 1 to 5.")


main()
