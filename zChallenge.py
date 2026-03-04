#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)


# this program creates an empty list and adds 40 numbers between 1 and 10 with a 50% chance of adding another number between 0.1 and 1.0