def bmi(kg,m):
    return kg/(m*m)
def check(kg,m=2, name="guest"):
    b=bmi(kg,m)
    print(name,"bmi",b)

check(60,1.5,name="bob")
check(60,1.5)
check(60)
#check()          #error:missing 1required position argument