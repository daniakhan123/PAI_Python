def divide_numbers():
    try:

        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

        div = num1 / num2
        print(f"The result of dividing {num1} by {num2} is {div}")

    except ZeroDivisionError:
        print("Division by zero is not possible.")
    except ValueError:
        print("Invalid input: Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
divide_numbers()
