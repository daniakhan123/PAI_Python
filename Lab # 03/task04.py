def biodata():
    try:
      
        name = input("Enter Name: ")
        cnic = input("Enter CNIC number: ")  
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        
      
        with open('info.txt', 'w') as file:
            file.write(f"Name: {name}\n")
            file.write(f"CNIC: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")
        
        
        contact_number = input("Enter Contact Number: ")
        with open('info.txt', 'a') as file:
            file.write(f"Contact Number: {contact_number}\n")
        
        
        with open('info.txt', 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    
    except ValueError as ve:
        print("Value Error: ")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print("An unexpected error occurred: ")
