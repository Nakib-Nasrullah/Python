a = "admin1"
b = "password1"

c = input("Enter your user name: ")
d = input("Enter your password: ")

e = "admin2"
f = "password2"

g = "admin3"
h = "password3"

if((c == a and d == b)or(c == e and d == f)or(c == g and d == h)):
    if(c == a):
        print("wellcome admin1")
    if(c == e):
        print("wellcome admin2")
    if(c == g):
        print("Wellcome admin3")
elif ((c != a and d == b)or(c != e and d == f)or(c != g and d == h)):       
    print("sorry!! your user name is worng!!")
elif ((c == a and d != b)or(c == e and d != f)or(c == g and d != h)):
    print("sorry!! your password is incorrect!!")
else:
    print("you are not the membre!!")
    