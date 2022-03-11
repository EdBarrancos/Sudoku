from log import *
from enum import Enum

class TableStyles(Enum):
    one_liner = 1
    matrix = 2

class Point:
    def __init__(self, x, y, value) -> None:
        self.x = x
        self.y = y
        self.CalculateSquare()
        self.value = value
        self.set = False if self.value == 0 else True
    
    def CalculateSquare(self):
        self.square = self.x // Sudoku.square_size + (self.y // Sudoku.square_size * 3)
    
    def IsSet(self):
        return self.set
    
    def UpdateValue(self):
        Logging.Section("UPDATE VALUE")

        self.value += 1
        if self.value > 9:
            self.value = 0

            Logging.Debug(f"New Value: {self.value}")
            
            return False

        Logging.Debug(f"New Value: {self.value}")

        return True

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            #If Points have the same coordenates, their the same point
            return self.x == __o.x and self.y == __o.y
        return False
    
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __str__(self) -> str:
        return f'({self.x},{self.y}) in square: {self.square} with value: {self.value}'

class Sudoku:
    sudoku_size = 9
    square_size = 3

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
            y = index // Sudoku.sudoku_size
            x = index - (Sudoku.sudoku_size * y)

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


    def Solve(self):
        actions = list()
        for point in self.points:

            Logging.Section("SOLVING")
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

        if not self.UpdatePoint(actions[pointer]):
                self.FixActions(actions, pointer - 1)

        while(not self.CheckPoint(actions[pointer])):
            if not self.UpdatePoint(actions[pointer]):
                self.FixActions(actions, pointer - 1)
        
    def UpdatePoint(self, point : Point):
        # TODO -> Visuals Update Shananigans
        return point.UpdateValue()

    def CheckPoint(self, point):
        Logging.Section("CHECK")

        if point.value == 0:
            return False

        return self.CheckPointLine(point) and self.CheckPointCollumn(point) and self.CheckPointSquare(point)

    def CheckPointLine(self, point):
        Logging.Section("CHECK LINE")

        Logging.Debug(f"Checking {point}")
        Logging.Info("Could use some performance improvements")

        check = True
        p_checked = 0
        for p in self.points:
            if p == point:
                continue
            if p.y == point.y:
                p_checked += 1
                if p.value == point.value:
                    check = False
                    break
            if p_checked == Sudoku.sudoku_size:
                break

        Logging.Debug(f'{check}')

        return check

    def CheckPointCollumn(self, point):
        Logging.Section("CHECK COLLUMN")

        Logging.Debug(f"Checking {point}")
        Logging.Info("Could use some performance improvements")

        check = True
        p_checked = 0
        for p in self.points:
            if p == point:
                continue
            if p.x == point.x:
                p_checked += 1
                if p.value == point.value:
                    check = False
                    break
            if p_checked == Sudoku.sudoku_size:
                break

        Logging.Debug(f'{check}')

        return check

    def CheckPointSquare(self, point):
        Logging.Section("CHECK SQUARE")

        Logging.Debug(f"Checking {point}")
        Logging.Info("Could use some performance improvements")

        check = True
        p_checked = 0
        for p in self.points:
            if p == point:
                continue
            if p.square == point.square:
                p_checked += 1
                if p.value == point.value:
                    check = False
                    break
            if p_checked == Sudoku.sudoku_size:
                break

        Logging.Debug(f'{check}')

        return check

    def StrOneLiner(self):
        result = str()
        for point in self.points:
            result += str(point.value)
        return result

    def StrMatrix(self):
        # TODO -> Finish
        Logging.Error("Soduku to matrix str not implemented yet")
        pass

    def __str__(self) -> str:
        if self.style == TableStyles.one_liner: return self.StrOneLiner()
        elif self.style == TableStyles.matrix: return self.StrMatrix()

