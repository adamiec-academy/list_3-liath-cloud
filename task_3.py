from random import randint
from turtle import *

speed('fast')

no_steps = 15
y_axis = [0, 15, 35, 50, 75, 105, 100, 70, 40, 35, 20, 5, 0]

for i in range(len(y_axis)):
    goto( i * no_steps, y_axis[i] + randint(-20, 20))

forward(20)

for i in range(len(y_axis), len(y_axis) * 2):
    goto( i * no_steps, y_axis[i - len(y_axis)] + randint(-20, 20))


exitonclick()
