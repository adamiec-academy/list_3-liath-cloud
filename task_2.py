def fibonacci_sequence(n):

    amount = 0
    result = []

    while amount != n:

        if n == 1:
            result.append(0)
            amount += 1

        elif n == 2 or amount < 2:
            result.append(0)
            result.append(1)
            amount += 2

        else:
            next = result[-1] + result[-2]
            result.append(next)
            amount += 1

    return result
