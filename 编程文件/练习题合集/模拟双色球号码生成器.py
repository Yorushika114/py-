import random

for i in range(0,5):
    rednum1 = random.randint(1, 33)
    print(f"\033[31m{rednum1}\033[0m",sep='' , end=' ')
bluenum1 = random.randint(1, 16)
print(f"\033[34m{bluenum1}\033[0m",sep='' , end=' ')