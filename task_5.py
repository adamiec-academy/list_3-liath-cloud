# Gwiazda 1

from turtle import *

speed('fast')

N = 16
M = 20
extra_length = 10

for i in range(N):

    length = 200

    for j in range(M):

        forward(length)
        backward(length)
        right((360/N)/M)

        length += extra_length

exitonclick()

# Gwaizda 2

from turtle import *

speed("fast")

def square(bok):

    left(90)

    for i in range(4):
        forward(bok)
        right(90)

def square_pyramid(bok, less, amount):

    height = 0

    for i in range(amount):

        height += bok
        square(bok)
        forward(bok)
        right(90)
        forward(less/2)

        bok -= less

    penup()
    forward(bok + (less/2) * 5)
    right(90)
    forward(height)
    left(90)
    pendown()

N = 6
bok = 50
less = 10
amount = 5

for i in range(N):

    square_pyramid(bok, less, amount)
    right(360/N)

exitonclick()

# Gwaizda 3

from turtle import *

speed('fast')

length = 250

for i in range(100):

    for j in range(5):
        forward(length)
        right(144)

    right(360/100)


exitonclick()
