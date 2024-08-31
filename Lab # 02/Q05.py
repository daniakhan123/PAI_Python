def fact(n):
    if(n == 0 or n== 1):
        print(1)
    elif(n>1):
        count = n
        while(count > 1):
            n = n * (count-1)
            count = count -1
        print("Facrorial is : ",n)  
    
    return 

n = int(input("Enter number : "))
fact(n)
