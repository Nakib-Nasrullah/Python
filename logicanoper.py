age = int(input("Inter your age: "))

if(age<18):
    print("You are a child")
elif(age>18 and age<40):
    print("You are a young!!")
elif(age>40 and age<100):
    print("You are an old!!")
else:
    print("You are already death!!")