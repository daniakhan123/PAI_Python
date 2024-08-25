
user_input = input('Enter numbers : ')
numbers = list(map(int, user_input.split()))

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1


print('Count of even numbers:', even_count)

