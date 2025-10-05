# Student name : Abdulaziz Mohammed Alkhlaiwe
# Student ID: 444101708

"""Write a program that asks the user to create a username and password, then allows three login attempts.
- Use a while loop for the attempts.
- After each incorrect login, display 'Incorrect credentials. Try again.'
- If the login succeeds, print 'Welcome, <username>!' using an f-string.
- After three failed attempts, print 'Access denied.'
Concepts: input/output, variables, conditions, f-strings, loops.
"""

def main():
    print("=== Account Setup ===")
    username = input("Create a username: ").strip()
    password = input("Create a password: ").strip()
    print("\n=== Login ===")
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        u = input("Username: ").strip()
        p = input("Password: ")
        if u == username and p == password:
            print(f"Welcome, {username}!")
            return
        attempts += 1
        if attempts < max_attempts:
            print("Incorrect credentials. Try again.")
    print("Access denied.")

if __name__ == "__main__":
    main()
