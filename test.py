print("hello world")
print("hello", "world")
print("hello","world",sep="-")
print("hello world","world",sep="$",end="&")

print(9//2)
print(9%5)
print(3**4)

a=1
b=2
print(a+b)

str1= "i am learning programming."
print(str1)
print(len(str1))

print(str1[2])
print(str1[5:13])
print(str1[5:])
print(str1[:13])
print(str1[:])
print(str1[::-1])

print("{0} {1}".format(100,200))
print("num1: {0} num2: {1}".format(a,b))
print("{0:10}{1:10}".format(200,300))
print("{0:<7}{1:>7}{2:>7}".format(12345,456,9998))

s = "Stone Campus"
# 這個字串的長度
# 位置 6 的字母 (使用 [])
print(len(s))
# 從位置 3 到 9 的子字串 "ne Camp" (使用[:])
print(s[6])
# 從位置 3 到 最後的子字串 "ne Campus" (使用[:])
print(s[3:])
# 從位置 0 到 9 的子字串 "Stone Camp"  (使用[:])
print(s[:])