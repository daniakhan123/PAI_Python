
def build_message(**info):
    message = "Details provided:\n"
    for key, value in info.items():
        message += f"{key.capitalize()}: {value}\n"
    return message

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print(build_message(name=name, age=age, city=city))
