# Student Grade Calculator

This project is a simple Python console application that asks for a student's name and marks, validates that the marks are between 0 and 100, then calculates a letter grade (A–F) and prints an encouraging message for the student.

---

## Project overview and objectives

The Student Grade Calculator is designed to quickly determine a student's grade based on their marks using clear grade ranges and friendly feedback messages.  
The main objectives of this project are:
- Use `if`, `elif`, and `else` statements to implement grading logic.
- Add input validation so only marks between 0 and 100 are accepted.
- Create and use at least one function to keep the logic organized.
- Display a formatted result that includes the student’s name, marks, grade, and an encouraging message.

---

## Setup and installation instructions


- A Python editor or IDE such as IDLE, VS Code, PyCharm, or Thonny.

### Steps to run the program

1. Download or clone this repository to your computer.
2. Make sure the following files are in the same folder:
   - `grade_calculator.py`
   - `test_cases.txt`
3. Open `grade_calculator.py` in your chosen editor or in IDLE.
4. Run the program:
   - In IDLE: press `F5` or choose **Run → Run Module**.
   - In terminal/command prompt:  
     `python grade_calculator.py`
5. Follow the on-screen prompts:
   - Enter the student’s name.
   - Enter the marks between 0 and 100.
  
6. The program will display the result in this style:



## Code structure explanation

### Files

- `grade_calculator.py`  
  Main Python script containing all the logic for:
  - Reading input from the user.
  - Validating the marks.
  - Calculating the grade.
  - Printing the formatted result and message.

- `test_cases.txt`  
  A text file listing manual test cases (sample inputs and expected outputs/behaviors) used to check that the program works correctly.

### Main functions and logic

- `calculate_grade_and_message(marks)`  
  - Input: a numeric `marks` value between 0 and 100.  
  - Output: a tuple `(grade, message)` where:
    - `grade` is one of `"A"`, `"B"`, `"C"`, `"D"`, `"F"`.
    - `message` is an encouraging sentence that matches the grade.  
  - Grading logic (using `if-elif-else`):
    - `marks >= 90` → Grade A → very strong positive message.
    - `marks >= 80` → Grade B → “Very Good! Keep it up!” style message.
    - `marks >= 70` → Grade C → “Good job” and “keep practicing” message.
    - `marks >= 60` → Grade D → “You passed” and “keep working” message.
    - Otherwise        → Grade F → supportive “don’t give up / try again” message.

- `get_valid_marks()`  
  - Continuously asks the user to enter marks until valid input is provided.
  - Uses `try` / `except` to catch non-numeric values.
  - Checks that `0 <= marks <= 100`.
  - Prints error messages for:
    - Non-numeric input.
    - Marks outside the 0–100 range.
  - Returns a valid numeric marks value.

- `main()`  
  - Prints a title: “Student Grade Calculator”.
  - Asks for the student’s name.
  - Calls `get_valid_marks()` to safely read the marks.
  - Calls `calculate_grade_and_message(marks)` to get the grade and message.
  - Converts the student’s name to uppercase for the result heading.
  - Prints a formatted result block, including:
    - The student’s name in uppercase.
    - Marks out of 100.
    - Letter grade.
    - Encouraging message.

This structure separates concerns: one function for grading, one for validation, and one main entry point that coordinates everything.

---

