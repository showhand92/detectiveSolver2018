import numpy as np
from collections import Counter

numToChar = { 1:'A', 2:'B', 3:'C', 4:'D'}
charToNum = {'A':1, 'B':2, 'C':3, 'D':4}

def gen():
    Ans = np.random.randint(1,5,size=10)
    AnsList = ['Blank']
    AnsList += [ numToChar[An] for An in Ans]
    return AnsList

def q2(AnsList):
    q2_dict = {'A':'C', 'B':'D', 'C':'A', 'D':'B'}
    return q2_dict[AnsList[2]] == AnsList[5]

def q3(AnsList):
    q3_dict = {'A': 3, 'B': 6, 'C': 2, 'D': 4}
    res = AnsList[q3_dict[AnsList[3]]]
    resList = [ int(res == AnsList[an]) for an in q3_dict.values()]
    return sum(resList)==1

def q4(AnsList):
    q4_dict = {'A':(1,5), 'B':(2,7), 'C':(1,9), 'D':(6,10)}
    an1, an2 = q4_dict[AnsList[4]]
    return AnsList[an1]==AnsList[an2]

def q5(AnsList):
    q5_dict = {'A':8, 'B':4, 'C':9, 'D':7}
    return AnsList[q5_dict[AnsList[5]]] == AnsList[5]

def q6(AnsList):
    q6_dict = {'A':(2,4), 'B':(1,6), 'C':(3,10), 'D':(5,9)}
    an1, an2 = q6_dict[AnsList[6]]
    return AnsList[an1]== AnsList[an2] and AnsList[8]==AnsList[an2]

def q7(AnsList):
    q7_dict = {'A':'C', 'B':'B', 'C':'A', 'D':'D'}
    a = q7_dict[AnsList[7]]
    b = Counter(AnsList[1:])
    for cha in ['A', 'B', 'C', 'D']:
        b[cha]+=1
    return a == b.most_common()[-1][0]

def q8(AnsList):
    q8_dict = {'A':7, 'B':5, 'C':2, 'D':10}
    return abs(charToNum[AnsList[q8_dict[AnsList[8]]]] - charToNum[AnsList[1]]) != 1

def q9(AnsList):
    q9_dict = {'A': 6, 'B': 10, 'C': 2, 'D': 9}
    return (AnsList[1] == AnsList[6])!= (AnsList[q9_dict[AnsList[9]]]==AnsList[5])

def q10(AnsList):
    q10_dict = {'A':3, 'B':2, 'C':4, 'D':1}
    count = np.array(Counter(AnsList).values())
    return  q10_dict[AnsList[10]] == np.max(count) - np.min(count)

def qAll(AnsList):
    myQuestions = [q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for i in range(9):
        if myQuestions[i](AnsList) == False:
            #print("Question "+str(i+2) + " failed")
            return False
    return True

def test():
    #AnsList = gen()
    #print(AnsList)
    #print(q10(AnsList))
    TrueList = [ 'Blank','B', 'C', 'A', 'C', 'A', 'C', 'D', 'A', 'B', 'A']
    print(TrueList)
    print(qAll(TrueList))

def solve():
    count = 0
    ans = {}
    while count < 20:
        AnsList = gen()
        done = qAll(AnsList)
        if done == True:
            ans[tuple(AnsList)] = True
            count += 1
            print(count)
    for l in ans.keys():
        print(l)

if __name__ == '__main__':
    #test()
    solve()
