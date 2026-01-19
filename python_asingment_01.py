class Course:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.__password = password
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        self.save_to_file()

    def get_password(self):
        return self.__password

    def save_to_file(self):
        with open("students.txt", "a") as f:
            course_names = ", ".join([c.name for c in self.courses])
            f.write(f"{self.name} | Roll: {self.roll} | Courses: {course_names}\n")

def show_all_students():
    print("===== All Students =====")
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No student data found.")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("students.txt file not found. No data available yet.")

def main():
    while True:
        print("\n===== School Management System =====")
        print("1. Enroll Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter student roll: ")
            password = input("Set password for student: ")
            student = Student(name, roll, password)

            num_courses = int(input("How many courses to enroll? "))
            for i in range(num_courses):
                course_name = input(f"Enter course {i+1} name: ")
                course = Course(course_name)
                student.enroll_course(course)

            print(f"Student {name} enrolled successfully!\n")

        elif choice == "2":
            show_all_students()

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
