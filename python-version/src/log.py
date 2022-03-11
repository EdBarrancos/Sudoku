from enum import Enum
from functools import total_ordering


ENDC = '\033[0m'

CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[33m'
PURPLE = '\033[35m'

colors = [CYAN, GREEN, RED, PURPLE]


BOLD = '\033[1m'
UNDERLINE = '\033[4m'

@total_ordering
class Level(Enum):
    ZERO = 1
    ERROR = 2
    DEBUG = 3
    INFO = 4

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented



class Logging:
    section = "MAIN"
    level = Level.ZERO
    currentColorI = 0
    newSection = False


    def SetUp(level_ : Level):
        Logging.level = level_

    def Section(sectionName : str):
        Logging.section = sectionName.upper()
        Logging.newSection = True
        Logging.nextColor()
    
    def CheckForNewSection():
        if Logging.newSection:
            print()
            Logging.newSection = False
    
    def nextColor():
        Logging.currentColorI += 1
        if Logging.currentColorI >= len(colors):
            Logging.currentColorI = 0

    def Error(message : str):
        if Logging.level >= Level.ERROR:
            Logging.CheckForNewSection()
            print(f'{colors[Logging.currentColorI]}[{Logging.section}]{BOLD}{UNDERLINE}|ERROR|{ENDC} {message} ')
    
    def Debug(message : str):
        if Logging.level >= Level.DEBUG:
            Logging.CheckForNewSection()
            print(f'{colors[Logging.currentColorI]}[{Logging.section}]{BOLD}|DEBUG|{ENDC} {message} ')

    def Info(message : str):
        if Logging.level >= Level.INFO:
            Logging.CheckForNewSection()
            print(f'{colors[Logging.currentColorI]}[{Logging.section}]|INFO|{ENDC} {message} ')