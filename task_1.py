def get_perfect_numbers(n):
    result = []
    amount = 0
    no = 6

    while amount != n:
        dzielniki = [1]

        for i in range(2, no):
            if no % i == 0 and i not in dzielniki:
                dzielniki.append(i)


        if sum(dzielniki) == no:
            result.append(no)
            amount += 1

        no += 1
    return result
