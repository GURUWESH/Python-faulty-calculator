a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
c=input("enter the operator")
if a==45 and b==3 and c=="*":
    print(555)
elif a==56 and b==9 and c=="+" :
    print(72)
elif a==56 and b==6 and c=="/":
    print(4)
else:
    if c=="*":
        print(a*b)
    elif c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="/":
        print(a/b)
    else:
        print("Enter a valid operator")
