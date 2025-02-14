#if condition
a=int(input("Enter a number"))
if a>0:
    print("positive")
#if and else condition
age=int(input("Enter a number"))
if age>=18:
    print("right to vote")
else:
    print("no right to vote")
#if elif else condition
a=int(input("Enter a number"))
if a%3==0 and a%5==0:
    print(" number is divisible by both 3 and 5")
elif a%3==0:
    print("number is divisible by 3")
elif a%5==0:
    print(" number is divisibl by 5")
else:
    print("none")
