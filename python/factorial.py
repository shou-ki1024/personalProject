#1! = 1
#2! = 2 * 1
#3! = 3 * 2 * 1

def fact(x:int):
    result = 1
    if x > 0:
        for i in range(x, 0, -1):
            result *= i
        print(result)
    else:
        for i in range(x, 0, +1):
            result *= -i
        print(-result)


x = int(input())
fact(x)

