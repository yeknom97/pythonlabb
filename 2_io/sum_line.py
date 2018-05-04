import sys

def sum_lines():
    for line in sys.stdin:
        line = line.strip()
        #print(line)
        tokens = line.split()
        #print(tokens)


        #total = sum([float(token) for token in tokens])

        total = 0
        for i in range(0, len(tokens)):
            total+=float (tokens[i])
        print(total)

sum_lines()