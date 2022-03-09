from distutils.log import Log
import sys
from log import *

MIN_ARGS = 2
MAX_ARGS = 4

""" Argument 1 -> Input file
    Argument 2 -> Output[Optional]
    Argument 3 -> Debug[Optional] """

if __name__ == "__main__":
    assert len(sys.argv) >= MIN_ARGS, "Argument Missing"
    assert len(sys.argv) <= MAX_ARGS, "Too many Arguments"

    output = sys.stdout
    debug = None

    if len(sys.argv) >= 3:
        output = open(sys.argv[2], mode="w")
    
    if len(sys.argv) >= 4:
        debug = open(sys.agrv[3], mode="r")

    #Logging.SetUp(Level.ERROR)

    # MAIN CODE

    fin = open(sys.argv[1], mode="r")
    if int(fin.read()) == 0:
        Logging.Debug("One hello")
        Logging.Info("asasdfsgh hello")
        Logging.Error("there was an Error")

        Logging.Section("Test")

        Logging.Debug("One hello")
        Logging.Info("asasdfsgh hello")
        Logging.Error("there was an Error")

        print("1",end="", file=output)
    else:
        Logging.Debug("One hello")
        Logging.Info("asasdfsgh hello")
        Logging.Error("there was an Error")

        Logging.Section("Test")

        Logging.Debug("One hello")
        Logging.Info("asasdfsgh hello")
        Logging.Error("there was an Error")

        print("0",end="", file=output)

    # MAIN CODE

    fin.close()
    if output:
        output.close()
    if debug:
        debug.close()


