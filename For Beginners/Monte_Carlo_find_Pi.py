import random

def estimate_pi():
    INTERVAL = int(input())
    points_in_circle = 0
    points_in_square = 0

    for i in range(INTERVAL):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x * x + y * y
        if distance <= 1:
            points_in_circle = points_in_circle + 1
        points_in_square = points_in_square + 1

        pi = 4 * points_in_circle / points_in_square

    print("Final Estimation of Pi=", pi)


estimate_pi()