#Testing ideas

class Matrix:
    def __init__(self, lst):
        """Initializes a matrix (Ax = b)
            Dict
                Ax -> Part Ax of the matrix
                b -> Part b of the matrix

        Args:
            lst -- list -- list of lists
        """
        self.matrix = dict()
        Ax = list()
        b = list()

        for value in lst:
            Ax.append(value[:-1])
            b.append(value[len(value) - 1])

        self.matrix['Ax'] = Ax
        self.matrix['b'] = b
        

    def get_line(self, line):
        """Returns a line of the Matrix

        Args:
            line -- int -- number of the line
        
        return a list with the values in the line
        """
        return [self.matrix['Ax'][line] + self.matrix['b'][line]]


    def get_collumn(self, collumn_nbr):
        """Returns a collumn of the Matrix

        Args:
            collumn_nbr -- int -- number of the collumn

        return a string
        """
        collumn = list()
        for i in range(self.matrix['Ax']):
            collumn.append(self.matrix['Ax'][i][collumn_nbr])

        return collumn

    
    def __repr__(self):
        """The representation of the matrix

        return a list with the values in the collumn
        """
        matrix_print = str()
        for line in range(len(self.matrix['Ax'])):
            for value in self.matrix['Ax'][line]:
                matrix_print += str(value) + "|"
            
            matrix_print += '|' + str(self.matrix['b'][line]) + '\n'
        
        return matrix_print[:-1]

a = [0,1,0,4]

b = [1,0,0,3]

c = [0,1,2,7]

matrix = Matrix([a,b,c])
print(matrix)



###############
#TESTING STUFF#
###############

def subtract(Li, Lj, alpha):
    """ Li = Li - alpha*Lj

        Args:
            Li,Lj -- list -- lines of the matrix
            alpha -- int -- number
    """
    if len(Li) != len(Lj):
        return "Not same length"

    for index in range(len(Li)):
        Li[index] -=  alpha*Lj[index]



def switch(Li, Lj, Matrix):
    """ Switches the position of Li and Lj in the Matrix

        Args:
            Li,Lj -- list -- lines of the matrix
            Matrix -- list of lists -- matirx
        
        return the Matrix
    """
    i = Matrix.index(Li)
    j = Matrix.index(Lj)

    Matrix[i] = Lj
    Matrix[j] = Li

    return Matrix



def is_simplified(Matrix):
    """ Checks if the Matrix is simplified

        Args:
            Matrix -- list of lists -- matirx
        
        return the bool
    """
    for j in range(len(Matrix[0])):
        if j != len(Matrix[0]) - 1:
            no_zero = False
            for i in range(len(Matrix)):
                if no_zero == False and Matrix[i][j] != 0:
                    no_zero = True
                elif no_zero == True and Matrix[i][j] != 0:
                    return False
        
    return True



def calculate_line(line, Matrix):
    """Calculates one of the line of the Matrix
        Args:
            line -- int -- number of the line to calculate
            Matrix -- list of lists -- matirx
        
        return the Matrix
    """
    collumn = 0
    if line != 0:
        collumn = find_collumn(Matrix, line)
                    #NOT WORKING PROPERLY
                    #MAKE A FUNCTION AND USE RETURN AS THE BREAKING POINT

    # print("collumn", collumn)

    collumn_done = False
    while collumn_done == False:
        for i in range(len(Matrix)):

            # print(Matrix)

            if Matrix[i][collumn] != 0:

                # print()
                # print("switch", Matrix[i], "with", Matrix[line])
                # print()

                Matrix = switch(Matrix[i], Matrix[line], Matrix)
                collumn_done = True
                break
        
        collumn += 1
    collumn -= 1

    # print()
    print("Matrix",Matrix)
    # print()

    #If there is one more line with a number different of zero in the collumn
    for i in range(len(Matrix)):
        if i != line:
            if Matrix[i][collumn] != 0:
                # print(Matrix[i][collumn])
                subtract(Matrix[i], Matrix[line], Matrix[i][collumn] / Matrix[line][collumn])
    
    # print("HERE IT GOES")
    return Matrix



def find_collumn(Matrix, line):
    for i in range(line):
        for j in range(len(Matrix[i])):
            if Matrix[i][j] != 0:
                collumn = j + 1
                return collumn
                


def simplify(Matrix):
    while True:
        #Check if the matrix is simplified
        if is_simplified(Matrix):
            break

        for i in range(len(Matrix)):
            if i != len(Matrix) - 1:
                Matrix = calculate_line(i, Matrix)
    
    return Matrix
