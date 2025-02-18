#How to declare different types of datatypes of datatypes
x=10 #interger(int)
print(type(x))
num=3.14#Float 
print(type(num))
num1=2+3j#complex
print(type(num1))
num2="python" #string(str)
print(type(num2))
num3=True #boolean (bool)
print(type(num3))
#List
mylist=[1,2,'python']
print(type(mylist))
#Tuple(tuple)
mytuple = (10, 20, "Hello")
print(type(mytuple))
#Set(set)
myset={1,2,3,4,5,6,7}
print(type(myset))
#Dictionary(dict)
mydict={"name":"sita","age":20}
print(type(mydict))
#None type
x=None
print(type(x))
#control statements
#using if statement
num4=5
if num4==5:
    print("Both are Equal")
else:
    print("Not Equal")  
num5=7
if num5==6:
    print("Both are Equal")
else:
    print("Not Equal") 
#using elif 
a=1
if a==0:
    print("zero")
elif a==1:
    print("one") 
elif a==2:
    print("Two")  
else:
    print("none") 
b=3
if b==0:
    print("zero")
elif b==1:
    print("one") 
elif b==2:
    print("Two")  
else:
    print("none")  
#loops 
# for loop

for i in range(0,20):
     print(i)
for i in range (0,30,2):#printing numbers by step(skip)
    print(i) 
#finding odd even numbers using for loop    
for i in range(0,50):
   if i%2==0 :
       print(i,"Even")  
   else:
       print(i,"odd")     
#while loop
two=5
while two<10:
    print(two,"postive")
    two+=1
div=5
while div<30:
    if div%5==0:
        print(div,"divisible by 5")
    else:
        print(div,"not divisible by5") 
    div+=1           
#functions declaring call function
def greet():
    print("Hello world")
greet()#calling a function
#function using parameters and arguments
def fun(name):#parameters
    print("hello,", name) 
fun("sita")  #argument
def add(a,b):
    print(a+b)
add(2,3)         
#using return statements
def sub(a,b):
    return a-b
print(sub(5,3))
#jump statements
#Break
k=1
while k<=10:
    if k==5:
        print(k)
        break        
    k+=1
    print(k)
print(k)
for r in range(1,11):
    if r==6:
        print(r)
        break
    print(r)
    
#continue
for num11 in range(1,6):
    if num11==3:
        print(num11)
        continue
    print(num11)