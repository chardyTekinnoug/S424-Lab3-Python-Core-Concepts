# Student name : Abdulaziz Mohammed Alkhlaiwe
# Student ID: 444101708

"""
Create a function get_average(marks) that returns the average of a list of grades entered by the user.
Your main program should:
1. Ask the user to enter marks separated by spaces (e.g. '85 90 78').
2. Convert them to integers inside a try/except block to handle invalid entries.
3. Call the function and print the average to two decimals.
Concepts: lists, split(), loops, functions, exceptions, formatted output.
"""


def get_average(marks):
    """Return the average of a list of grades."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def main():
    try:
        # Step 1: Ask user to enter marks separated by spaces
        user_input = input("Enter marks separated by spaces (e.g. '85 90 78'): ")

        # Step 2: Convert to integers (handle invalid entries)
        marks = [int(x) for x in user_input.split()]

        # Step 3: Calculate and print average to two decimals
        average = get_average(marks)
        print(f"Average: {average:.2f}")

    except ValueError:
        print("Invalid input. Please enter only integer numbers.")


if __name__ == "__main__":
    main()
