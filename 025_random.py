import random
from tkinter import Y

for i in range(5):
    print(random.random())

for i in range(5):
    print(random.randint(0, 10))

# challange 1: choose the leader
candidtes = ['surajit', 'akshay', 'shaw', 'piklu', 'riya']
leader = random.choice(candidtes)
print(leader)


# challange 2
x = random.randint(0, 100)
y = random.randint(0, 100)
print(f'({x}, {y})')