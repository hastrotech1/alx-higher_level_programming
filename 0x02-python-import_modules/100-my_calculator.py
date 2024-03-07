#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def calculate(argv):
    
    cal_len = len(argv) - 1
    
    if cal_len != 3:

        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        
        exit(1)

    a = int(argv[1])

    operat_or = argv[2]

    b = int(argv[3])

    if operat_or == '+':
        
        print("{:d} {:s} {:d} = {:d}".format(a, operat_or, b, add(a, b)))
        
    elif operat_or == '-':
        
        print("{:d} {:s} {:d} = {:d}".format(a, operat_or, b, sub(a, b)))
        
    elif operat_or == '*':
        
        print("{:d} {:s} {:d} = {:d}".format(a, operat_or, b, mul(a, b)))
        
    elif operat_or == '/':
        
        print("{:d} {:s} {:d} = {:d}".format(a, operat_or, b, div(a, b)))
        
    else:
        
        print("Unknown operator. Available operators: +, -, * and /")
        
        exit(1)

        
if __name__ == "__main__":
    
    import sys
    
    calculate(sys.argv)
