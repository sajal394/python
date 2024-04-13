# variables are case sensitive

roll = 21
ROLL = 22
Roll = 23
print(roll, ROLL, Roll)

x, y = 1, 2
print(1, 2)

a = b = c = 10
print(a, b, c)

# delete a variable
d = 10
print(d)
del d

# short hand operators
count = 0
count = count + 1
count = count + 1
count = count + 1
count = count + 1
print(count)

# above code can be written like this:
count1 = 0
count1 += 1
count1 += 1
count1 += 1
count1 += 1
print(count1)

# in operator
print('sajal' in 'i am sajal goel')
print('anmol' in 'i am aakash')

# Expressions=> chanining operators

e = 5
print(1 < e < 10)
print(10 < e < 20)
