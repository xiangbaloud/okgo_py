#!/usr/bin/python
def fib(n):
    list_a = [0, 1]
    for i in range(n):
        x = list_a[-1] + list_a[-2]
        list_a.append(x)
    return list_a

print(fib(17))
