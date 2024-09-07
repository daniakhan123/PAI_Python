def replaceWord(filename, wordfind, repword):
    try:
        with open('text.txt', 'r') as file:
            content = file.read()
        
        newContent= content.replace(wordfind, repword)
        
        with open(filename, 'w') as file:
            file.write(newContent)
        
        print("All occurrences have been replaced")
    
    except FileNotFoundError:
        print("Error: The file  was not found.")
    except IOError:
        print("Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print("An unexpected error occurred")


wordfind = 'python'
repword = 'Cpp'
replaceWord('text.txt', wordfind, repword)
