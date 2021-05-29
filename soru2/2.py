op_file = open('toplamlar.txt','w')

def digits(nb1):

    total = 0

    while nb1 > 0:
        total += nb1 % 10
        nb1 = int(nb1 / 10)

    return total


with open('sayilar.txt','r') as file:
    line = file.readline()

    while line:
        number = digits(int(line.strip()))
        op_file.write(str(number))

        while len(str(number)) > 1:
            number = digits(number)
            op_file.write(" " + str(number))

        op_file.write("\n")

        line = file.readline()