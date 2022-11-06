def tower(n):
    max_length = 1 + 2 * (n - 1)
    space = int((max_length - 1) / 2)
    symbol_no = 1

    for i in range(n):
        line = ""
        line += " " * space + "#" * symbol_no + " " * space

        space -= 1
        symbol_no += 2

        for j in range(3):
            print(line)


def towers(data):
    maxymalna = max(data)

    length_part = [0 for k in range(len(data))]

    inx = 0
    for i in data:

        for j in range(1, i+1):

            if j == 1:
                length_part[inx] += 1
            else:
                length_part[inx] += 2

        inx += 1
    odliczanie = maxymalna

    kratki = [0 for k in range(len(data))]

    for i in range(maxymalna):

        linia = ""

        for j in data:

            if j < odliczanie:
                linia += " " * length_part[data.index(j)]

            elif j == odliczanie:
                length_part[data.index(j)] = length_part[data.index(j)] - 1

                if data[data.index(j)] > 1:
                    linia += " " * int((length_part[data.index(j)]/2)) + "#" + " " * int(((length_part[data.index(j)])/2))
                    kratki[data.index(j)] += 1
                else:
                    linia += "#"
                    kratki[data.index(j)] += 1
            else:
                length_part[data.index(j)] = length_part[data.index(j)] - 2
                kratki[data.index(j)] += 2
                linia += " " * int(((length_part[data.index(j)])/2)) + "#" * int(kratki[data.index(j)]) + " " * int(((length_part[data.index(j)])/2))

            linia += " "

        odliczanie -= 1

        for l in range(3):
            print(linia[0:-1])
