#!/usr/bin/python

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def main():
    print "Options:"
    print " 1) addition"
    print " 2) subtraction"
    print " 3) multiplication"
    print " 4) division"
    option = input("select your option: ")
    options = [1, 2, 3, 4]
    if option not in options:
        print "invalid option" 
        exit()
    else:
        pass        
    x = input("input your first number: ")
    y = input("input your second number: ")
    if option == 1:
        print x, "+", y, "=", addition(x, y)
    elif option == 2:
        print x, "-", y, "=", subtraction(x, y)
    elif option == 3:
        print x, "*", y, "=", multiplication(x, y)
    elif option == 4:
        print x, "/", y, "=", division(x, y)
    else:
        print "invalid option"

if __name__ == '__main__':
    main()
