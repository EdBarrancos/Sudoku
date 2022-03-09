from distutils.log import Log
import sys
from log import *

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

    if len(sys.argv) >= 3:
        output = open(sys.argv[2], mode="w")
    
    #Initialize Debugging Level
    if len(sys.argv) >= 4:
        if sys.argv[3] == "-i":
            Logging.SetUp(Level.INFO)
        elif sys.argv[3] == "-d":
            Logging.SetUp(Level.DEBUG)
        elif sys.argv[3] == "-e":
            Logging.SetUp(Level.ERROR)

    return output

if __name__ == "__main__":
    output = ParseArgs()

    fin = open(sys.argv[1], mode="r")

    #############
    # MAIN CODE #
    #############
    
    print("#RESULT#", file=output)

    #############
    # MAIN CODE #
    #############

    fin.close()
    if output:
        output.close()


