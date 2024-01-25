while(True):
    print("*****Calculator*****\nMenu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    x=int(input("Enter your choice "))                                                                         
    temp=x  
    if temp == 1 :
        a=int(input("Enter 1st number:- "))
        b=int(input("Enter 2nd number:- "))
        c=a+b
        print ("Addition = ",c)  
    elif temp == 2 :
        a=int(input("Enter 1st number:- "))
        b=int(input("Enter 2nd number:- "))
        c=a-b
        print("Subtraction = ",c)    
    elif temp == 3 :
        a=int(input("Enter 1st number:- "))
        b=int(input("Enter 2nd number:- "))
        c=a*b
        print("Multiplication = ",c)
    elif temp == 4 :
        a=int(input("Enter 1st number:- "))
        b=int(input("Enter 2nd number:- "))
        c=a/b
        d=a%b
        print("Qutient = ",int(c))
        print("Remainder = ",d) 
    elif temp == 5 :
        print("Invalid")
        break
