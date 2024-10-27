   
for i in range(0, 10, 1):
    if (i==5 or i==8):
        continue
    print("This is for loop", i)
else:
    print("This is the end of for loop")
    
for i in range(0, 10, 1):
    print("This is for loop", i)
    if i==5:
        break
else:
    print("This is the end of cod")
    