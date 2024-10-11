import random

def check(lef,rig):
    if lef > rig:
        if lef==rig+1: 
            return "Bの勝ち"
        elif lef==rig+2:
            return "Aの勝ち"
        else:
            return "Bの勝ち"
    if rig > lef:
        if rig==lef+1:
            return "Aの勝ち"
        elif rig==lef+2:
            return "Bの勝ち"
        else:
            return "Aの勝ち"
    else:
        return "引き分け"

def replacepoint(x):
    y=str(x)
    y=y.replace("0","グー")
    y=y.replace("1","チョキ")
    y=y.replace("2","パー")
    return y

countA=0
countB=0
for i in range(3):
    A=random.randint(0,2)
    B=random.randint(0,2)
    result=check(A,B)
    A=replacepoint(A)
    B=replacepoint(B)

    print("Aの⼿︓"+A+" v.s. Bの⼿︓"+B)
    print(result)
    if result == "Aの勝ち":
        countA += 1
    elif result == "Bの勝ち":
        countB += 1
if countA>countB:
    print("結果:Aの勝利")
elif countA==countB:
    print("結果:引き分け!")
else:
    print("結果:Bの勝利")