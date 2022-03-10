from log import *
from enum import Enum

class TableStyles(Enum):
    one_liner = 1
    matrix = 2

class Point:
    def __init__(self, x, y, value) -> None:
        self.x = x
        self.y = y
        self.square = self.CalculateSquare()
        self.value = value
        self.set = False if self.value == 0 else True
    
    def CalculateSquare(self):
        # TODO -> Finish
        Logging.Error("Calculate Point's Square not implemented yet")
        pass
    
    def IsSet(self):
        return self.set
    
    def UpdateValue(self):
        # TODO -> Finish
        Logging.Error("Update Point's Value not implemented yet")
        pass

    def __str__(self) -> str:
        return f'({self.x},{self.y}) in square: {self.square} with value: {self.value}'

class Sudoku:
    def __init__(self, raw_sudoku) -> None:
        self.sudoku = self.CreateTable(raw_sudoku)
    
    def CreateTable(self, raw_sudoku):
        """ Creates The Table From strings

            Formating Rules:
                - Empty spaces as 0's or other characters besides numbers
                - As a One Liner or a Matrix
        """

        Logging.Section("SET_UP")

        self.points = list()

        if len(raw_sudoku) == 1:
            self.style = TableStyles.one_liner
            self.CreateTableFromOneLiner(raw_sudoku)
        else:
            self.style = TableStyles.matrix
            self.CreateTableFromMatrix(raw_sudoku)

    def CreateTableFromOneLiner(self, raw_sudoku):
        for index in range(len(raw_sudoku[0])):
            Logging.Info(f'Creating from index: {index}')
            y = index // 9
            x = index - (9 * y)

            if raw_sudoku[0][index].isdigit():
                value = int(raw_sudoku[0][index])
            else:
                value = 0
            
            point = Point(x, y, value)

            Logging.Debug(f'Point: {point} created')

            self.points.append(point)
            
        
    def CreateTableFromMatrix(self, raw_sudoku):
        # TODO -> FINISH
        Logging.Error("Create Table From Matrix not implemented yet")
        pass


    def Solve(self, listPoints):
        actions = list()
        for point in listPoints:
            if not point.IsSet():
                Logging.Info("Add point as changed")
                actions.append(point)
                
                Logging.Info("Change it until it fits if we reach 0 -> Fix Others")
                while(not self.CheckPoint(point)):
                    if not self.UpdatePoint(point):
                        self.FixActions(actions, len(actions) - 2) #Point to the last to the end

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
        Logging.Error("Check Point not implemented yet")
        pass

    def StrOneLiner(self):
        result = str()
        for point in self.points:
            result.append(point.value)

    def StrMatrix(self):
        # TODO -> Finish
        Logging.Error("Soduku to matrix str not implemented yet")
        pass

    def __str__(self) -> str:
        if self.style == TableStyles.one_liner: return self.StrOneLiner()
        elif self.style == TableStyles.matrix: return self.StrMatrix()

