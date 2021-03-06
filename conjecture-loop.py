from time import sleep
def conundrum(n):
    t=n
    iteration = 0
    while True:
        iteration += 1
        if t%2 == 0:
            t /= 2
        else:
            t *= 3
            t += 1
        if iteration%3 == 0:
            print(t)
        else:
            print(t, end=", ")
        sleep(.4)

n = int(input("Please enter a number of your choice: "))
conundrum(n)
