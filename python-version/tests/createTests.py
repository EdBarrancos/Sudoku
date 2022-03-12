import os

OKGREEN = '\033[92m'
ENDC = '\033[0m'

INPUT_FILE_DEST = "tests/inputs"
if not os.path.exists(INPUT_FILE_DEST):
    os.mkdir(INPUT_FILE_DEST)
OUTPUT_FILE_DEST = "tests/outputs"
if not os.path.exists(OUTPUT_FILE_DEST):
    os.mkdir(OUTPUT_FILE_DEST)

# TODO -> Fix: Kinda Bad, doesn't accept only "\n"

def GetName():
    name = str(input("Name of the Tests: "))
    while name == "\n":
        name = str(input("Name of the Tests: "))
    return name

def GetI(name):
    i = 0
    while os.path.exists(f'{INPUT_FILE_DEST}/{name}{i}'):
        i += 1
    return i

def GetInput():
    result = str(input("What will be input(-1 to stop): "))
    while result == "\n":
        result = str(input())
    return result

def GetOuput():
    output = str(input("Pretended Output: "))
    while output == "\n":
        output = str(input())
    return output

TESTS_NAME = GetName()

i = GetI(TESTS_NAME)
test = GetInput()
while test != "-1":
    f = open(f'{INPUT_FILE_DEST}/{TESTS_NAME}{i}', mode="w")
    f.write(test)
    f.close()

    test = GetOuput()
    f = open(f'{OUTPUT_FILE_DEST}/{TESTS_NAME}{i}', mode="w")
    f.write(test)
    f.close()

    print(f'{OKGREEN}TEST {TESTS_NAME}{i} CREATED WITH SUCCESS{ENDC}')

    i += 1
    test = GetInput()
