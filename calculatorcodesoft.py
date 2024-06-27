# Function to perform the calculations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        return num1 / num2
    else:
        return "Invalid operation"


# Main function to drive the calculator
def main():
    # Prompt user for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user for the operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation
    result = calculate(num1, num2, operation)

    # Display the result
    print(f"The result is: {result}")


# Run the main function
if __name__ == "__main__":
    main()
