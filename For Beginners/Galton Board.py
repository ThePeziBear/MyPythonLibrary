import matplotlib.pyplot as plt
import random

balls = 100  # number of balls
p = 0.5


def distribution(p):
    choice = random.uniform(0, 1)
    if choice < p:
        choice = 1
    else:
        choice = 0
    return choice


def galton(balls, p):
    result = []
    for i in range(0, balls):
        course = 0
        for x in range(0, 10):
            choice = distribution(p)
            if choice == 1:
                course = course + 1

        result.append(course)
    return result


x=galton(balls,p)
y=[1,2,3,4,5,6,7,8,9,10]

fig, axs = plt.subplots(sharey=True, tight_layout=True)
axs.hist(x, bins=y)
