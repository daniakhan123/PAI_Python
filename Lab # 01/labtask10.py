
user = input("Enter a list of numbers: ")
str_list = user.split()

num_list = []
for num_str in str_list:
    num_list.append(int(num_str))

largestnum = max(num_list)
print("The largest number is:", largestnum)
