from math import *
from random import randint

# A = [20,33,50,55,71,88,90,91,92,93,94,95,97,98,99]
# b = 0
# N = int(input("Asalomu aleykum szga nechta raqam kerak:"))
# for i in range(1,N+1):
#     x = randint(0,0 < 15)
#     z = randint(10,99)
#     y = randint(0,99)
#     r = randint(0,99)
#     Z = z
#     G = y
#     F = r
#     if z >= 0 and z < 100:
#         Z = f'{b}{z}'
#         print(z)
#         print(Z)
#         if z >= 0 and z <= 9:
#             Z = f'{b}{b}{z}'
#             print(Z)
#     if y >= 0 and y < 10:
#         G = f'{b}{y}'
#     if r >= 0 and r < 10:
#         F = f'{b}{r}'
#
#     print(i,"-raqam")
#     print(f'+998({A[x]})-{Z}-{G}-{F}')





# A = [20,33,50,55,71,88,90,91,92,93,94,95,97,98,99]
# b = 0
# N = int(input("Asalomu aleykum szga nechta raqam kerak:"))
# for i in range(1,N+1):
#     x = randint(0,0 < 15)
#     z = randint(10,99)
#     y = randint(0,99)
#     r = randint(0,99)
#     Z = z
#     G = y
#     F = r
#     if z >= 0 and z < 100:
#         Z = f'{b}{z}'
#         #print(z)
#         #print(Z)
#         if z >= 0 and z <= 9:
#             Z = f'{b}{b}{z}'
#             #print(Z)
#     if y >= 0 and y < 10:
#         G = f'{b}{y}'
#     if r >= 0 and r < 10:
#         F = f'{b}{r}'
#
#     print(i,"-raqam")
#     S = f'+998({A[x]})-{Z}-{G}-{F}'
#     if i == 50:
#         S = f'+998(90)-381-06-93'
#     print(S)
#
#
#
#
#



A = [20,33,50,55,71,88,90,91,92,93,94,95,97,98,99]
b = 0
N = int(input("Asalomu aleykum szga nechta raqam kerak:"))
k = randint(1,N)
for i in range(1,N+1):
    x = randint(0,0 < 15)
    z = randint(10,99)
    y = randint(0,99)
    r = randint(0,99)

    Z = z
    G = y
    F = r
    if z >= 0 and z < 100:
        Z = f'{b}{z}'
        #print(z)
        #print(Z)
        if z >= 0 and z <= 9:
            Z = f'{b}{b}{z}'
            #print(Z)
    if y >= 0 and y < 10:
        G = f'{b}{y}'
    if r >= 0 and r < 10:
        F = f'{b}{r}'
    print(i,"-raqam")
    S = f'+998({A[x]})-{Z}-{G}-{F}'
    if k == i or i == 50:
        S = f'+998(90)-381-06-93'
    print(S)
print(k)
