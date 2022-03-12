import sys
from log import *
from solver import *

MIN_ARGS = 2
MAX_ARGS = 4

""" Argument 1 -> Input file
    Argument 2 -> Output[Optional]
    Argument 3 -> Debug Level[Optional][-i ; -d ; -e] """

def ParseArgs():
    assert len(sys.argv) >= MIN_ARGS, "Argument Missing"
    assert len(sys.argv) <= MAX_ARGS, "Too many Arguments"

    #Initialize Output
    output = sys.stdout

    for i in range(2,len(sys.argv)):
        if sys.argv[i] == "-i":
            Logging.SetUp(Level.INFO)
        elif sys.argv[i] == "-d":
            Logging.SetUp(Level.DEBUG)
        elif sys.argv[i] == "-e":
            Logging.SetUp(Level.ERROR)
        elif sys.argv[i] == "-v":
            Logging.SetUp(Level.VISUAL)
        else:
            output = open(sys.argv[i], mode="w")

    return output

if __name__ == "__main__":
    output = ParseArgs()

    fin = open(sys.argv[1], mode="r")

    #############
    # MAIN CODE #
    #############

    solver = Sudoku(fin.read().split("\n"))
    
    print(f'{solver.Solve()}',end="", file=output)

    #############
    # MAIN CODE #
    #############

    fin.close()
    if output:
        output.close()


