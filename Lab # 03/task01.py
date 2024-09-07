try:
    with open('text1.txt', 'r') as file:
        content = file.read()

    num_characters = len(content)
  
    print(f"Total number of characters: {num_characters}")

except FileNotFoundError:
    print("Error: The file  was not found.")
except IOError:
    print("Error: There was an issue reading the file.")
except Exception as e:
    print("An unexpected error occurred")
