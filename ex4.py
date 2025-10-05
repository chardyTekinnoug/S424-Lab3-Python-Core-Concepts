# Student name : Abdulaziz Mohammed Alkhlaiwe
# Student ID: 444101708

"""
Define a class BankAccount with:
- Attributes: owner, balance (initialized to 0).
- Methods:
- deposit(amount) → adds to balance.
- withdraw(amount) → subtracts only if sufficient funds; otherwise raise a ValueError.
- display() → prints the current balance using an f-string.
In the main program, create an account, perform deposits/withdrawals, and handle exceptions gracefully.
Concepts: classes, methods, objects, self, exception handling, encapsulation logic.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def display(self) -> None:
        print(f"{self.owner}'s current balance: {self.balance:.2f}")

def main():
    print("=== Create Bank Account ===")
    owner = input("Enter account owner's name: ").strip() or "Unknown Owner"
    account = BankAccount(owner)

    while True:
        print("\n=== Bank Menu ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == "1":
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)
                print("Deposit successful.")
            elif choice == "2":
                amt = float(input("Enter withdrawal amount: "))
                account.withdraw(amt)
                print("Withdrawal successful.")
            elif choice == "3":
                account.display()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-4.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
