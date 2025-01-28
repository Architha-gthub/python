#complex numbers
a=5+1j
b=9+10j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
#In complex numbers (// and % will not work)
#print(a%b)-unsupported operand type(s) for %: 'complex' and 'complex'
#print(a//b)-It shows TypeError: unsupported operand type(s) for //: 'complex' and 'complex

#Boolean Expressions
#it will have only True or False
a=25
print(a==35)
print(a==25)
print(a>3)
print(a<14)
print(a>=24)
print(45>43)
print(50<25)
print(19>=19)
print(56<=55)

#Sequences - Strings, List, Tuples, Range

#List- List is a ordered collection of data items and it can be changeable (Mutable)
list=[0,3,4,'String',True,[1,"Hello",3]]
print(id(list)) 
print(type(list))
print(len(list))
print(list)
print(list[2]) 
print(list[5])

#print(list[6]) #shows IndexError: list index out of range, because the given list consists of only 5 indices

print(list[0:8:2])
print(list[-5])
print(list[5][0]) #Accessing list inside list
print(len(list[5])) #length of list inside list
list[4]="False" #changing the value of index 4,list is a mutable datatype so, it can be change.
print(list)
list[5][1]="Bye" #changing the value of index 1 inside index 5
print(list[5])
print(len(list[5][1])) #length of "hello" insode inner list

#Tuple - Tuple is ordered collection of data items but unchangeable (Immutable)
tuple=(1,2,3,[1,2,3],"tuple")
print(tuple)
print(id(tuple))
print(type(tuple))
print(len(tuple))
print(tuple[3])
print(tuple[-1])

#tuple[3]='5'
#print(tuple) #It shows TypeError: 'tuple' object does not support item assignment, because tuple is immutable(cannot be change)
#Range - Limit
#list = [1, 2, 3] Overwrites the built-in list function
#print(list(range(0, 100)))  # Causes TypeError because 'list' is now a variable, not a function
#print(list(range(0,100,2)))
#print("----Range----")
#print(list(range(0,100,2))) #skips 1 number and then it prints
#print(list(range(100,0,-3))) #skips 2 and then prints in reverse order
#print(list(range(100,0,-1))) #prints continous and then print in reverse order
#print(list(range(100,-1))) #prints empty list (because 1st number is greater than 2nd number, if we need to print then give -1 then it print in reverse order)
list=[1,2,4,6,5,85]
print(len(list))
for i in range(0,len(list)):
    #print(i)
    print(i,list[i])

#for i in range(0,100):
    #print(i)

print("----Dictionary----") #--> Collection of items, which is used to store items in key value pair, we can access through keys only(Mutable data type)
dict={1:'Mahesh Babu',2:'AA',3:'Dhanush',4:'Rajendra Prasad',5:'Snow Family',6:'Surya',7:'Surya'}

print(dict[2])
print(dict)
#Changing the value of key-1
dict[1]='BB2'
print(dict) #It can be change the value of Mahesh babu to BB2 because, dictionary is mutable data type.

#To add key:value pair in dictionary(at the end of dictionary)
dict['key-1']='value-1'
print(dict)

#If we need to update the key-1 value to updated value
dict['key-1']='updated-value-1'
print(dict) # It can be replace in place of value-1

print("----Set----")
#Set-Collection of elements(Unique, Unordered, Finite) and it is Immutable data type

set={2,4,5,2,2,2,2,4,6}
print(set) #Repeated elements will be prints at one time only

print("----None----")
num=5
num=None
print(num)
print(type(num))
print(id(num)) #It prints memeory but there is nothing in this memory, because num stores 'None'

#input()

print(input("Enter a number"))

#refer input to a variable

a=input("Enter a number")
print(a)

a=int(input("Enter a value"))
b=int(input("Enter a value"))
print(a+b)