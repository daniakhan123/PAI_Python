user = input("Enter URL : ")

print("original URl : " ,user)

if user.startswith("http://www."):
    user2 = user.removeprefix("http://www.")
    new = user2 + '.com'
    print("New URL : " , new)
    
