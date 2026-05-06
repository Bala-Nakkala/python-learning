numbers = [10]
colours = ['red', 'blue', 'green']
names = ('John', 'Jane', 'Doe')
fruits = {'apple', 'banana', 'cherry'}
for c in colours:
    print(c)
for nu in numbers:
    print(nu)
for n in names:
    print(n)
for f in fruits:
    print(f)
######################################
numbers = [1, 2, 3, 4, 5,]
for n in numbers:
    if n == 3:
        break       
    print(n)

######################################
for n in numbers:
    if n == 3:
        continue       
    print(n)


###############################

i = 0
while i < 5:
    print(i)
    i += 1  