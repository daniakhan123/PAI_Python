import json

try:
    dictionary = {
        'Ali': 23,
        'Saad': 24,
        'Salman': 15,
        'Shams': 25,
        'Sadiq': 46,
        'Hammad': 23
    }

    with open('q5.txt', 'w+') as file:
        json.dump(dictionary, file)
        file.seek(0)
        data = json.load(file)

    print("File: ")
    print(data)

    listKeys = list(data.keys())
    listVals = list(data.values())

    
    max_age = max(listVals)
    print("The maximum age is:", max_age)


    print("DUPLICATES: ")

    for i in range(len(listVals)):
        for j in range(i + 1, len(listVals)):
            if listVals[i] == listVals[j]:

                print(f"Age {listVals[i]} is duplicated by {listKeys[i]} and {listKeys[j]}")

except NameError:
    print(f"name of file is not defined")
except FileNotFoundError:
    print(f"Error: The file  was not found.")
except ValueError:
    print("That's not a valid integer. Please try again.")
except Exception as e:
     print("An unexpected error occurred: ")
