user_cur = int(input("Which curency you want to convert from Enter :  \n [1] for EURO \n [2] for DOLLAR \n [3] for PKR \n [4] for INR \n [5] for YEN \n"))

if(user_cur == 1):
    user_amount = float(input("Enter your amount : "))
    currency = int(input("Which curency you want to convert to Enter : \n [1] for DOLLAR \n [2] for PKR \n [3] for INR \n [4] for YEN \n"))
    if(currency == 1):
        dollar = user_amount * 1.11
        print("Your Amount in Dollar  is : ",dollar)
    elif(currency == 2):
        pkr = user_amount * 308
        print("Your Amount in PKR  is : ",pkr)
    elif(currency == 3):
        inr = user_amount * 92.67
        print("Your Amount in INR is : ",inr)
    elif(currency == 4):
        yen = user_amount * 161.74
        print("Your Amount in YEN  is : ",yen)
        
elif(user_cur == 2):
    user_amount = float(input("Enter your amount : "))
    currency = int(input("Which curency you want to convert to Enter :  \n [1] for EURO  \n [2] for PKR \n [3] for INR \n [4] for YEN \n"))
    if(currency == 1):
        euro = user_amount * 0.91
        print("Your Amount in Euro  is : ",euro)
    elif(currency == 2):
        pkr = user_amount * 285.0
        print("Your Amount in PKR  is : ",pkr)
    elif(currency == 3):
        inr = user_amount * 80.0
        print("Your Amount in INR is : ",inr)
    elif(currency == 4):
        yen = user_amount * 145.0
        print("Your Amount in YEN  is : ",yen)
        
elif(user_cur == 3):
    user_amount = float(input("Enter your amount : "))
    currency = int(input("Which curency you want to convert to Enter :  \n [1] for EURO \n [2] for DOLLAR \n [3] for INR \n [4] for YEN \n"))
    if(currency == 1):
        euro = user_amount * 0.0032
        print("Your Amount in Euro  is : ",euro)
    elif(currency == 2):
        dollar = user_amount * 0.0035
        print("Your Amount in Dollar  is : ",dollar)
    elif(currency == 3):
        inr = user_amount * 0.28
        print("Your Amount in INR is : ",inr)
    elif(currency == 4):
        yen = user_amount * 0.51
        print("Your Amount in YEN  is : ",yen)
        
elif(user_cur == 4):
    user_amount = float(input("Enter your amount : "))
    currency = int(input("Which curency you want to convert to Enter :  \n [1] for EURO \n [2] for DOLLAR \n [3] for PKR \n [4] for YEN \n"))
    if(currency == 1):
        euro = user_amount * 0.011
        print("Your Amount in Euro  is : ",euro)
    elif(currency == 2):
        dollar = user_amount * 0.0125
        print("Your Amount in Dollar  is : ",dollar)
    elif(currency == 3):
        pkr = user_amount * 3.57
        print("Your Amount in PKR  is : ",pkr)
    elif(currency == 4):
        yen = user_amount * 1.8
        print("Your Amount in YEN  is : ",yen)
        
elif(user_cur == 5):
    user_amount = float(input("Enter your amount : "))
    currency = int(input("Which curency you want to convert to Enter :  \n [1] for EURO \n [2] for DOLLAR \n [3] for PKR \n [4] for INR \n"))
    if(currency == 1):
        euro = user_amount * 0.0063
        print("Your Amount in Euro  is : ",euro)
    elif(currency == 2):
        dollar = user_amount *  0.0069
        print("Your Amount in Dollar  is : ",dollar)
    elif(currency == 3):
        pkr = user_amount *1.98
        print("Your Amount in PKR  is : ",pkr)
    elif(currency == 4):
        inr = user_amount * 0.56
        print("Your Amount in INR is : ",inr)

