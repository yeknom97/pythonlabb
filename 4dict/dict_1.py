ages = {}

def prage(name):
    if(ages.get(name)):
        print(name,ages.get(name))
    else:
        print("N/A")


def test():
    num = int(input())
    for i in range(0,num):
        line = input()
        tokens = line.strip().split()
        name = tokens[0]
        age = int(tokens[1])
        ages[name] = age
    print(ages)
    # print name and age
    num = int(input())
    for i in range(0, num):
        line = input()
        print(ages.get(name))
        

test()