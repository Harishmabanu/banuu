num = input("Enter year:");
if num=='x':
    exit();
try:
    year=int(num);
except ValueError:
    print("enter the year...existing");
else:
    if((year%4==0) and (year%100!=0)):
        print(year, "is a Leap Year.");
    elif((year%100==0) and (year%400==0)):
    	print(year,"is a Leap Year.");
    elif(year%400==0):
    	print(year,"yes");
    else:
    	print(year,"no");
