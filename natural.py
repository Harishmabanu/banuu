num = int(input("sum of natural number:"));
if num==0:
    exit();
elif num<1:
    print("enter a positive number..exiting..");
else:
    sum=0;
    while num>0:
    	sum +=num;
    	num -=1;
    print(sum);
