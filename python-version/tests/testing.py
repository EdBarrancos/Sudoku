from cgi import test
import difflib
import subprocess
import os
from glob import glob


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
OKRED = '\033[33m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def PrintFail(arg, name):
    if arg == False:
        print(f"{OKRED}{BOLD}\t-->\t{name.upper()} FAILED{ENDC}\n\n")
    return True

def PrintPass(name):
    print(f'{OKGREEN}{BOLD}\t-->\t{name.upper()} PASSED{ENDC}\n\n')

FILES = glob("tests/inputs/*")

print(f"\n\t -----------------", f"\n\t{BOLD}{UNDERLINE}TESTING ./src/main.py{ENDC}\n",f"\t-----------------\n\n")

test_statistics = {"total": 0, "failed": 0, "passed": 0}

for file in FILES:
    test_statistics["total"] += 1
    _,name = os.path.split(file)
    print(f'{OKBLUE}{name.upper()} --| {ENDC}')
    os.system(f"python3 src/main.py {file} tests/tmp/{name}")
    
    output = open(f"tests/outputs/{name}").readlines()
    tmp = open(f"tests/tmp/{name}").readlines()

    thereIsDiff = False
    for line in difflib.unified_diff(output,tmp):
        thereIsDiff = PrintFail(thereIsDiff, name)
        print(line)
    if not thereIsDiff:
        PrintPass(name)
        test_statistics["passed"] += 1
    else:
        test_statistics["failed"] += 1

print()

if test_statistics["failed"] > 0:
    print(f'{BOLD}{OKRED}\tTEST FAILED -> TOTAL: {test_statistics["total"]} | PASSED: {test_statistics["passed"]} | FAILED: {test_statistics["failed"]}')
else:
    print(f'{BOLD}{OKGREEN}\tTEST PASSED -> TOTAL: {test_statistics["total"]} | PASSED: {test_statistics["passed"]} | FAILED: {test_statistics["failed"]}')
    
print()
print()