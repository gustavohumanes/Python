import random
for num in range(10):
    num = random.gauss(mu=175, sigma=7) 
    print(f"{num:.2f}")