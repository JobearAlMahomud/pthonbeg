from operator import truediv

#string
var = 'I am writing python'
print(var)

#Examples of Datatype on python.

#intiger data type

inti = 420
print(inti)

print(type(inti))

# floating type data

float = 40.20

print (float)

print (type(float))

# Complex Type data
complex = 420j

print(complex)
print(type(complex))

#strig type data
MyName = "Jobear "
YoureName = "James"

print(MyName + YoureName)
print(type(MyName + YoureName))

#Boolean data type
Bool = True
print(Bool)
print(type(Bool))

x = 10
y = 10
print(x>y)
print(x==y)


#binary type data byte
list = [1,2,3,4,5,6,7,8,10,255]
b = bytes(list)
print(type(b))

#binaru type data byte array
list1 = [1,2,3,4,5,6,7,8,10,255]
b1 = bytearray(list1)
print(type(b1))
print(b1[1])
#changes on array
b1[1] = 100
print(b1[1])

#None type data
x= None
print(type(x))
print(x)
