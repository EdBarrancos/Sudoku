from log import *

class Point:
    def __init__(self) -> None:
        # TODO -> Finish
        self.x = 0
        self.y = 0
        self.square = 0
        self.value = 0
        self.set = False
    
    def IsSet(self):
        return self.set
    
    def UpdateValue(self):
        # TODO -> Finish
        pass

class Sudoku:
    def __init__(self) -> None:
        self.sudoku = self.CreateTable()
    
    def CreateTable(self):
        self.points = list()
        # TODO -> FINISH
        pass

    def Solve(self, listPoints):
        actions = list(9)
        for point in listPoints:
            if not point.IsSet():
                Logging.Info("Add to point as changed")
                actions.append(point)
                
                Logging.Info("Change it until it fits if we reach 0 -> Fix Others")
                while(not self.CheckPoint(point)):
                    if not self.UpdatePoint(point):
                        self.FixActions(actions, len(actions) - 2)

        Logging.Debug("Finished")
        return self
        
    
    def FixActions(self, actions, pointer):
        Logging.Debug(f"Begin Fix on Pointer: {pointer}")
        if pointer == -1:
            Logging.Error("Unsolvable Soduku")

        while(not self.CheckPoint(actions[pointer])):
            if not self.UpdatePoint(actions[pointer]):
                self.FixActions(actions, pointer - 1)
        
    def UpdatePoint(point):
        point.UpdateValue()
        # TODO -> Visuals Update Shananigans

    def CheckPoint(self, point):
        # TODO -> Finish
        pass

    def __str__(self) -> str:
        # TODO -> Finish
        pass

