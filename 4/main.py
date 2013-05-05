from math import sin
from simpsons import Simpsons

FUNCTION = lambda x : sin(3*x) 

def main():
    simpsons = Simpsons(FUNCTION, 2, 1, 0)

if __name__ == "__main__":
    main()