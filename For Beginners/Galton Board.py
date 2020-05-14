from random import randint as ri

balls = 100  # number of balls
slots = 10  # number of base slots
# you can edit the values for different size of board, and different number of balls

res = []

for i in range(slots):
    res.append(0)

for i in range(balls):
    subres = [1]
    for j in range(slots - 1):
        subres.insert((j + 1) * ri(0, 1), 0)
    res[subres.index(1)] += 1
# subres is a subresult of one ball. '1' is the position of the ball. in each galton row it goes left or right - practically there is randomly an additional '0' at the beginning or at the end. 'res' collects each ball's 'subres'

for i in range(slots):
    print((1 + slots - i) * ' ' + i * '. ')
# hey what a picturesque Galton board!

for i in range(max(res) + 1, 0, -1):
    [print('|o', end='') if j >= i else print('| ', end='') for j in res]
    print('|')
print('-' * (2 * slots + 1))
# and here are the balls arrived to the slots. the only reason you missed the cool animation the mass of balls bouncing downwards is that python is so fast and you don't! ;)

print(res)
