class NegativeAgeException(Exception):
    pass

def generate_student_details():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        if age < 0:
            raise NegativeAgeException("Age must be positive.")

        marks = {}
        for i in range(1, 7):
            subject = input("Enter subject {}: ".format(i))
            subject_marks = float(input("Enter marks for {}: ".format(subject)))
            marks[subject] = subject_marks

        student_details = {
            "Name": name,
            "Age": age,
            "Marks": marks
        }

        print("Student details:", student_details)

    except NegativeAgeException as e:
        print("Error:", str(e))
    except ValueError:
        print("Error: Invalid input for age or marks.")

# Example usage
generate_student_details()
