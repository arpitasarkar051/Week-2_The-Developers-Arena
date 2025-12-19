# Student Grade Calculator

This project is a simple Python console application that takes a student's marks, validates that the value is between 0 and 100, calculates the letter grade using if-elif-else statements, and displays an encouraging message based on the result.

---

## Setup and installation

Steps (example for IDLE / any IDE):

1. Open `grade_calculator.py` in IDLE or your preferred IDE.
2. Run the script (for example, press `F5` in IDLE).
3. When prompted, enter student marks between 0 and 100 and press Enter.

No external libraries are required; only the Python standard library is used.[web:19]

---

## Code structure explanation

Main files:
- `grade_calculator.py`  
  - `calculate_grade_and_message(marks)`:  
    - Input: numeric marks between 0 and 100.  
    - Output: a tuple `(grade, message)`.  
    - Logic: uses an if-elif-else chain:
      - 90–100 → A with a very positive message.  
      - 80–89 → B with an encouraging message.  
      - 70–79 → C with a “good effort” message.  
      - 60–69 → D with “you passed, work more” message.  
      - 0–59  → F with a supportive “try again” message.[web:11][web:10]
  - `get_valid_marks()`:
    - Uses a `while True` loop to repeatedly ask for input.
    - Uses `try` / `except ValueError` to ensure the input is numeric.[web:10]
    - Checks that `0 <= marks <= 100`; if not, prints an error and asks again.
  - `main()`:
    - Prints a title.
    - Calls `get_valid_marks()` to read and validate the marks.
    - Calls `calculate_grade_and_message(marks)` to compute the grade and message.
    - Prints marks, grade, and the encouraging message.

- `test_cases.txt`  
  - Contains sample inputs and the expected grade/message type to help manually test the program.

This structure keeps grading logic inside a dedicated function and separates user input, validation, and output into different parts, which is recommended for clear, beginner-friendly Python projects.[web:16]

---

## Screenshots of working application

Add screenshots to show the program running for different cases. For example:

 Create a folder named `screenshots` in your repository.


