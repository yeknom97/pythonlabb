nums = [0, 1, 2, 3, 4]

#   [(x ** 2)for x in nums]
squares1 = [x * 2 for x in nums]
squares = [x ** 2 for x in nums]
print(squares1)
print(squares) #     prints [0, 1, 4, 9, 16]

nums = [-2, -1, 0, 1, 2]
#       abs(x) for...
ds = [abs(x) for x in nums if abs(x) < 2]
print(ds)      # prints [1, 0, 1]

from math import pi
print(pi)             # 3.141592653589793
print(round(pi, 3))  # 3.142
                #str(...)  for...
print([str(round(pi, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']



