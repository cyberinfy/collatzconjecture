from time import sleep
import sys

def conundrum(n):
    print(n, end="-> ")
    t=n
    iteration = 0
    while True:
        iteration += 1
        if t%2 == 0:
            t /= 2
        else:
            t *= 3
            t += 1
        if iteration<9 or t<4:
            print(t, end=", ")
        elif t==4:
            print("....,",t,end=", ")
        if t==1:
            break
    print()
    sleep(.1)

for i in range(1,sys.maxsize):
    conundrum(i)
