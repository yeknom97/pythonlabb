def result(answer, guess):
    A = 0
    B = 0
    for idxans, valans in enumerate(answer):
        for idxgue, valgue in enumerate(guess):
            #print(idxans,valans,idxgue,valgue)
            if valans==valgue:
                if idxans==idxgue:
                    A+=1
                else:
                    B+=1
    return str(A)+"A"+str(B)+"B"

print(result('1234','4321'))
print(result('4657','9658'))
print(result('9876','6879'))

def result1(answer, guess):
    A = 0
    B = 0
    for idxans, valans in enumerate(answer):
        if answer[idxans]==guess[idxans]:
            A+=1
        elif(valans in guess):            
                    B+=1
    return str(A)+"A"+str(B)+"B"

print(result1('1234','4321'))
print(result1('4657','9658'))
print(result1('9876','6879'))
