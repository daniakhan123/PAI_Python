def replace_letter():
    
    with open("replacement_needed.txt", "r") as file:
        data = file.read()

        print("Before replacement:")
        print(data)

    o_letter = input("Enter letter you want to replace: ")
    r_letter = input("Enter letter you want to replace with: ")

    try:
        new_data = data.replace(o_letter, r_letter)
    
        with open("replacement_needed.txt", "w") as file:
            file.write(new_data)
    
        print("After replacement:")
        print(new_data)
    
    except FileNotFoundError:
        print("Error The file was not found")
    except IOError:
        print("Error while opening the file")
    except Exception as e:
        print("An unexpected error occurred ")


replace_letter()

