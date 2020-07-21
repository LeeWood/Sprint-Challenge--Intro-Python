# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("\nStarts with D:")

a = []
for human in humans:
    if human.name[0].lower() == 'd': #making sure check is not case sensitive against original list. 
        a.append(human)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("\nEnds with e:")

b = []
for human in humans:
    if human.name[-1].lower() == 'e':
        b.append(human)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("\nStarts between C and G, inclusive:")

chars = [chr(i) for i in range(ord('c'), ord('g')+1)]

c = []
for human in humans:
    if human.name[0].lower() in chars:
        c.append(human) 

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("\nAges plus 10:")

d = []
for human in humans:
    d.append(int(human.age) + 10)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("\nName hyphen age:")

e = []
for human in humans:
    e.append(f'{human.name}-{human.age}')

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("\nNames and ages between 27 and 32:")

f = []
for human in humans:
    if human.age in range(27, 33):
        f.append(human)

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("\nAll names uppercase:")

g = []
for human in humans:
    g.append(f'{human.name.upper()}, {(human.age + 5)}')

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("\nSquare root of ages:")
import math

h = []
for human in humans:
    h.append(math.sqrt(human.age))

print(h)
