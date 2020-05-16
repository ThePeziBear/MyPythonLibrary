import matplotlib.pyplot as plt
import random

TOTAL_BALLS = 500
TOTAL_LINES = 10

for i in range(0, TOTAL_BALLS):
    total = []
    for i in range(0, TOTAL_LINES):

        x = random.uniform(0, 1)
        if x >= 0.5:
            round(x)
        else:
            round(x)

        total.append(round(x))

        distribution = sum(total)
        print(distribution)



