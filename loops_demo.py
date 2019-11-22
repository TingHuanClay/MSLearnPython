names = ['Clay', 'Sharon', 'Ruth']

"""
directly use the object of the collections for for loop
"""
for name in names:
    print(name)
print()

"""
use range() method to define the index in for loop
"""
for index in range(0,2):
    print(f"{index} : {names[index]}")
print()

"""
use len() method with while loop
"""
index = 0
while index < len(names):
    print(names[index])
    index = index + 1