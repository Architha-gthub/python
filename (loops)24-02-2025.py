#Question1
# Print all numbers from 1 to 100 using a  for  loop. 
sum=0
for i in range(1,101):
    print(i)
    sum=sum+i
print(sum) 
#Question2 
#Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 
n=10
print((n*(n+1))/2) 
#Question3 
#Print all even numbers between 1 and 50 using a  while loop.
num=0
while num<=50:
    if(num%2==0):
     print(num)
    num+=1  
#Question4
#Write a program to display the multiplication table of a given number. First 20 
for num1 in range(1,11):
   for j in range(1,11):
      print(num1,'*',j,'=',num1*j) 
#Question5
#Reverse a number using a  while  loop. 
#1.Also can we get the sum of all the digits.   
num2=56723
digits_sum=0
reverse=0
count=0
while num2>0:
   rem=num2%10 
   digits_sum+=rem
   reverse=reverse*10+rem
   num2//=10
   count+=1
if reverse==num2:
   print("Palindrome") 
else:
   print("Not a palindrome")     
print("Reversed number:", reverse)
print("sum of digits:",digits_sum) 
print("no of digits:",count) 
#Question6 
# write a program to count the number of digits in a given number using a  while  loop.
num3=1234567
counts=0
while num3>0:
   num3//=10
   counts+=1
print("No of digits:", counts)  
#Question7
#Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop.
num1 = int(input("enter a number: "))
while(num1>0):
    num1 = int(input("enter the number: "))
print(num1)
# Medium queries
# Question1
# Print the first 10 terms of the Fibonacci series using a  for loop. 
a, b = 0, 1  
for _ in range(10): 
    print(a, end=" ")
    a, b = b, a + b
#for single number
def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(1))  
print(fibonacci_recursive(15))
#Question2
#Check if a given number is a prime number using a  for loop. 
num = int(input("Enter a number: "))
if(num==1):
    print("1 is neither prime nor composite")
else:
    isprime = True
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    if isprime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
#Question3
# Write a program to calculate the factorial of a number using a  while  loop. 
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"factorial of {num} is {fact}")
#Question4
#print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop.
    
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
#Question5
#Implement a menu-driven program where the user can 
# choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit. 
print('''choose to: 
1.  Find the square of a number. 
2.  Find the cube of a number. 
3.  Exit.''')
choice = int(input("enter your choice: "))
if(choice==1):
    print("you chose to find the sqaure of a number: ")
    num = int(input("enter the number: "))
    print(f"square of {num} is {num*num}")
elif(choice==2):
    print("you chose to find the cube of a number: ")
    num = int(input("enter the number: "))
    print(f"cube of {num} is {num*num*num}")
else:
    print("EXITED SUCCESSFULLY!!!")
#Question6
#Implement a basic login system where the user has three attempts to enter the correct password using a loop.
attempts = 3
password = "123456"
print("Hello login here!!!")
while attempts!=0:
    enter = input("enter the password : ")
    if(password==enter):
        print("Login successfull")
        break
    else:
        print("Invalid password:(")
        attempts-=1
if(attempts==0):
    print("You have reached maximum limit of attempts!!!!")    