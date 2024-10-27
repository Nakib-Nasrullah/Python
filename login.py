a = "admin1" #admin 1 Username
b = "password123" #admin 1 password

e = "admin2"
f = "pass1234"

c = input("Enter your username: ")
d = input("Enter your password: ")

if ((c == a and d == b) or (c == e and d == f)):
    if(c == a):
        print("Wellcome admin1")
    if(c == e):
        print("wellcome admin2")
elif((c == a and d != b) or (c == e and d != f)):
    print("worng password!! please enter your correct password!!")
elif((c != a and d == b) or (c != e and d == f)):
    print("Yoir admin name is worng!! enter your correct admin mane!!")
else:
    print("You are not a member")