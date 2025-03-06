#Q1)Find the sum of odd digits in a given number
num=123456789
sum=0
while num>0:
    digit=num%10
    if digit%2!=0:
        sum+=digit
    num//=10    
print(sum)      
#Q2)Print all the Armstrong numbers in given range
minnum=int(input("Enter a minnum"))  
maxnum=int(input("Enter a maxnum"))
for num in range(minnum,maxnum+1):
    tem=num
    sum=0
    while tem>0:
        digit=tem%10
        sum+=digit**len(str(num)) 
        tem//=10
    if(sum==num):
        print(num,"is a amstrong number")     
#Q3)Find the smallest prime digit in a given number  
num = int(input("Enter a number: "))
smallprimenum = 10
while num > 0:
    digit = num % 10
    if digit in (2, 3, 5, 7) and digit < smallprimenum:
        smallprimenum = digit
    num //= 10
if smallprimenum == 10:
    print("No prime digits found.")
else:
    print("The smallest prime digit is:", smallprimenum)         

