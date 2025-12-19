# grade_calculator.py

def calculate_grade_and_message(marks):
    """
    Take numeric marks (0-100) and return (grade, message) tuple.
    """
    if marks >= 90:
        grade = "A"
        message = "Excellent! You are a star learner!"
    elif marks >= 80:
        grade = "B"
        message = "Very Good! Keep it up!"
    elif marks >= 70:
        grade = "C"
        message = "Good job! Keep practicing and you will do even better."
    elif marks >= 60:
        grade = "D"
        message = "You passed. Keep working and you will improve."
    else:
        grade = "F"
        message = "Don't give up. Learn from this and try again!"

    return grade, message


def get_valid_marks():
    """
    Ask the user for marks until a valid number between 0 and 100 is entered.
    Returns marks as a float.
    """
    while True:
        raw_input_value = input("Enter marks (0-100): ")

        try:
            marks = float(raw_input_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value for marks.")
            continue

        if 0 <= marks <= 100:
            return marks
        else:
            print("Marks must be between 0 and 100. Please try again.")


def main():
    print("=== Student Grade Calculator ===")
    student_name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade_and_message(marks)

    # Name in uppercase for the title line
    name_upper = student_name.upper()  # standard string method to uppercase text[web:39]

    print(f"\n📊 RESULT FOR {name_upper}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()
