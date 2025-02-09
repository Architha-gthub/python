#operators
#logical operators-and,or,not
#and opertor
# in and operator if first operator is false output is false.
#if both operators are true output also will be true.
#if first operator will True and sceond operator is false then output will be false.
#even  if one operator is false then output will false.
# if a is true then output depends on (a and b).
#if a is false then oput return false.it will not check other operator.
#Examples for AND operator:
print(True and True)
print(False and False) 
print(True and False)
print(False and True)
print(True and(False and True))
print(False and (True and True))
print(True and(True and True))
print(True and (True and False))
print(False and (False and False))
#using numbers
print(3 and 1)
print(1 and 3)
print(-1 and 3)
print(3 and-5)
print(0 and -1)
print(0 and 5)
print(0 and "")
print("" and 0)
print("" and 5)
print(6 and "")
print(-6 and "")
print("hello" and "hi")
print("True" and "empty")
print("None" and 3)
print(3 and"None")

#Or operator-if any one operator is true output will be true
print(True or True)
print(False or False)
print(True or False)
print(False or True)
#using numbers
print(2 or 3)# if both operators are true it will print first operator
print(3 or -1)
print(-1 or 5)
print(-9 or -4)
print(0 or -1)
print(1 or 0)
print("None" or 0)
print(0 or "None")
print(False or (True and False))
print(False and(True or False))
print(True and(False or True))
print(True or(False and False))
# Not Operator
print(not True)
print(not False)
print(not(2 or 3))
print(not (20 and 3))
print(not("" and 3))
#Bitwise Operators
# &,|,^,~,>>,<<
print(4&3)#4-0100&3=>0011=0
print(12&14)#1100&1110=>1100=12
print(12 | 14)#|-or=>1100|1110=>1110-14
print(12^14)#^-indicates Xor
print(3 << 1)#left shift
print(3 >> 1)#right shift
print(4 << 1)#left shift
print(4 >> 1)#right shift