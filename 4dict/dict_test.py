ages = {}
ages['bob'] = 9
ages['alice'] = 18

ages['bob']              # 9
print(ages['bob'])
print(ages.get('bob'))
print(ages.get('john','N/A'))
print(len(ages))
print(list(ages))
print('bob' in ages)
print('john' in  ages)



#ages.bob                 # error: 'dict' object has no attribute 'bob'
ages.get('bob')          # 9
ages['john']             # KeyError: 'john'
ages.get('john')         # None
ages.get('john', 'N/A')  # 'N/A'
len(ages)                # 2
list(ages)               # ['bob', 'alice'], order may differ
'bob' in ages            # True
'john' in ages           # False