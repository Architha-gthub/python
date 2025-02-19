#Easy Qestions
#Question1
a=int(input("Enter a number"))
if a>0:
     print("positive number")
elif a==0:
    print("zero")
else:
     print("Negative number")  
#Question2
num=int(input("Enter a number"))
if num%2==0:
    print(num,"even")
else:
    print(num,"odd") 
#Question3
age =int(input("enter your age")) 
if age>=18:
    print("Eligible to vote" )
else:
    print("Not eligible for vote")
#Question4
a=float(input("Enter a number"))
b=float(input("Enter a number"))
if a<b:
    print(a,"is lessthan of" ,b)
elif a<b:
    print(b,"is greater than",a) 
else:
     print("Both are Equal")   
#Question5
score=float(input("Enter a ypur score"))
if score>40:
     print("pass")
else:
    print("fail")    
# or
marks=41
marks="pass" if marks>40 else "fail"          
#Question6
Days=int(input("Enter your Day"))
if Days==1:
     print("monday")
elif Days==2:
     print("Tuesday")
elif Days==3:
     print("wednesday")
elif Days==4:
     print("Thursday")
elif Days==5:
    print("Friday") 
elif Days==6:
    print("Stauraday") 
elif Days==7:
    print("Sunday")  
else:
    print("invalid input! Enter a number between 1 to 7")
#Question7
operation=input("Enter Your operation to perform between numbers 'add or sub or div'").lower()
x=int(input("Enter a number"))
y=20   
if operation == "add":
    print(x+y) 
elif operation=="sub":
    print(x-y)
elif operation=="div":
    if x==0:
        print("division is not possible")
    else:
        print(x/y)   
#Question8
month=int(input("Enter a digit"))
if month==1:
    print("janauary")
elif month==2:
    print("February")
elif month==3:
    print("March")
elif month==4:
    print("April")
elif month==5:
     print("may")
elif month==6:
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("August")        
elif month==9:
     print("September") 
elif month==10:
     print("October")
elif month==11:
     print("November")
elif month==12:
     print("December")
else:
     print("Enter a number in between 1 to 12") 
#medium questions
#Question 1
n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
n3=int(input("Enter a number"))
if n1>n2 and n1>n3:
    print(f"{n1} is greater than n1 and n3")  
elif n2>n1 and n2>n3:
     print(f"{n2} is greater than n1 and n3")
elif n3>n2 and n3>n1:
     print(f"{n3} is greater than n1 and n2")
#Question2
year=int(input("Enter a year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
     print(f'{year} is a leap year')
else:
     print(f'{year} is not a leap year')    
#Question 3
char = input("enter any single character").lower()
if len(char) != 1:
   print("invalid input")
elif char in ['a','e','i','o','u']:
     print("vowel")
elif char.isalpha():
    print("consonants")
else:
    print("special characters or symbols not accepted")
#Question 4
score=int(input("Enter your score"))
if score>=90 and score<=100:
    print("Grade A")   
elif score>=80 and score<=89:
    print("Grade B") 
elif score>=70 and score<=79:
    print("Grade C")
else:
    print("Fail")
#Question 5
s1=int(input("Enter a side one of triangle"))
s2=int(input("Enter a second side of triangle"))
s3=int(input("Enter a third side of triangle"))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        print("The given sides form a valid triangle.")
# Check the type of triangle
elif s1 == s2 == s3:
      print("It is an Equilateral Triangle.")
else:
     print("Not form a valid triangle")      