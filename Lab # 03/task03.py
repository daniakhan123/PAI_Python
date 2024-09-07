Keys = []
num = int(input("Enter number of elements of the list : "))
for i in range(num):
    Keys.append(input("Input elements : "))

values = []

for i in range(num):
    values.append(input("Input values "))

Dict={}
for i in range(num):
    Dict[Keys[i]]=values[i]
    
    
    try:
        with open("dict.txt" , 'w') as file:
            
            for key, value in Dict.items():
                file.write(f"{key}: {value}\n")
                
                
        print("dictionary hhas been added to a file")
    
    except FileNotFoundError:
        print("Error: The file  was not found.")
    except IOError:
        print("Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print("An unexpected error occurred")

