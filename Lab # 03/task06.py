def write_sentence():
    sentence = input("Enter any sentence : ")
    if sentence.endswith("?"):
        with open("questions.txt" , "a") as file:
            file.write(sentence + "\n")
            print("The question has been wrtitten")
try:
    write_sentence()
except FileNotFoundError:
    print("Error: The file  was not found.")
except IOError:
    print("Error: There was an issue reading the file.")
except Exception as e:
    print("An unexpected error occurred")
