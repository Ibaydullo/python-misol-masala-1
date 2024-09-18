
with open('citations.txt', 'r', encoding='utf-8') as f:
    #print(f.read())
    W = f.readlines()
for i in W:
    A = 0
    Y = 0
    T = 0
    J = 0
    I = 0
    S = 0
    E = 0
    if len(i) > 1 and i[0]=='A':
        A = i[6:]
    if len(i) > 1 and i[0]=='Y':
        Y = i[6:]
    if len(i) > 1 and i[0]== 'T':
        T = i[6:]
    if len(i) > 1 and i[0]=='J':
        J = i[6:]
    if len(i) > 1 and i[0]=='I':
        I = i[6:]
    if len(i) > 1 and i[0]=='S':
        S = i[6:]
    if len(i) > 1 and i[0]=='E':
        E = i[6:]

    print(A,Y,T,J,I,S,E)











