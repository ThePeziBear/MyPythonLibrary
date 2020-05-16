from random import randint
import matplotlib.pyplot as plt

balls = 100  # number of balls
levels = 10  # number of base slots


# you can edit the values for different size of board, and different number of balls
def galton():
    result = []
    for i in range(0, levels):
        result.append(0)

    for i in range(balls):
        course = [1]
        for x in range(levels):
            course.insert((x + 1) * randint(0, 1), 0)
        result[course.index(1)] += 1
    # subres is a subresult of one ball.
    # '1' is the position of the ball. in each galton row it goes left or right - practically there is randomly an additional
    # '0' at the beginning or at the end. 'res' collects each ball's 'subres'
    return result


galton()


