'''promblem1
'''
def prlist(arr):
    for idx,el in enumerate(arr):
        if(idx!=len(arr)-1):
            print(el,end=",")
        else:
            print(el)
a=[10,20,30,40,50]
b=[30,4,56]
prlist(a)
prlist(b)

''' problem2
'''
def enumlist(arr):
    #1. apple
    for idx,el in enumerate(arr):
        print(idx+1,".",el)
        print("{}. {}".format(idx+1,el))
enumlist(['apple','orange','banana'])
