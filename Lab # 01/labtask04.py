numbers = []

print('Enter numbers one by one. Type "done" when finished:')

while True:

    user_input = input('Enter a number: ')


    if user_input.lower() == 'done':
        break

    try:

        number = float(user_input)
        numbers.append(number)
    except ValueError:

        print('Invalid input. Please enter a valid number.')

total_sum = sum(numbers)

print('Sum of all elements:', total_sum)
