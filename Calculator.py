class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Cannot divide by zero."


def main():
    calculator = Calculator()

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print("Result:", calculator.add(num1, num2))
            elif choice == '2':
                print("Result:", calculator.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calculator.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calculator.divide(num1, num2))

            break
        else:
            print("Invalid input. Please enter a valid choice.")


if __name__ == '__main__':
    main()