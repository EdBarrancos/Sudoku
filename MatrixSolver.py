############################################################################
############################################################################

########
#MATRIX#
########

class Matrix:
    def __init__(self, lst):
        """Initializes a matrix (Ax = b)
            Dict
                Ax -> Part Ax of the matrix
                b -> Part b of the matrix

            Args:
                lst -- list -- list of lists
        """

        ###########
        #AUXILIARY#
        ###########

        def verify_args(lst):
            '''Verifies the arguments given to create the matrix

                Args:
                Same as the matrix

                returns bool
            '''

            if isinstance(lst, list):
                #The Argument has to be a list
                size = 0

                for line in lst:
                    if isinstance(line, list):
                        #Each Value in the main list also has to be a list
                        if len(line) >= 2:
                            #The list sizes have to be at least two or greater
                            if size != 0:
                                #The size variable is already set
                                if len(line) == size:
                                    #All lines have to have the same size
                                    for index in range(len(line)):
                                            if not isinstance(line[index], int):
                                                #All the values have to be intengers
                                                return False
                                else:
                                    #Not all lines have the same size
                                    return False
                            else:
                                #Set the size variable
                                size = len(line)                  
                    else:
                        #Not all the Values in the main list are lists
                        return False
            else:
                #The Argument isn't a list
                return False

            #Passed all tests
            return True

        if verify_args(lst):
            self.matrix = dict()
            Ax = list()
            b = list()

            for value in lst:
                Ax.append(value[:-1])
                b.append(value[len(value) - 1])

            self.matrix['Ax'] = Ax
            self.matrix['b'] = b
        else:
            raise ValueError ("Matrix, __init__: argument not valid")

    def get_line(self, line):
        """Returns a line of the Matrix

        Args:
            line -- int -- number of the line
        
        return a list 
        """
        return self.matrix['Ax'][line] + [self.matrix['b'][line]]


    def get_collumn(self, collumn_nbr):
        """Returns a collumn of the Matrix

        Args:
            collumn_nbr -- int -- number of the collumn

        return a list
        """
        if collumn_nbr >= len(self.matrix['Ax'][0]):
            #Only the collumn with the results
            return self.matrix['b']
        else:
            collumn = list()
            for i in range(len(self.matrix['Ax'])):
                collumn.append(self.matrix['Ax'][i][collumn_nbr])

            return collumn
    

    def get_size(self):
        """The x and y size of the matrix

        return a dict 
        """
        return {'y': len(self.get_collumn(0)),'x': len(self.matrix['Ax']) + 1}
    

    def get_line_Ax(self, line_nbr):
        '''Returns only the Ax part of the line

        Args:
            line_nbr -- int -- number of the line

        return list
        '''
        line = self.get_line(line_nbr)

        return line[:-1]

    def change_line(self, line_nbr, new_line):
        '''Changes destroctively the line in the line_nbr with new_line

            Args:
                line_nbr -- int -- number of the line to be changed
                new_line -- list -- new line

            return self
        '''

        new_matrix = list()
        for index in range(self.get_size()['y']):
            if index == line_nbr:
                #The line that needs changing
                new_matrix.append(new_line)
            else:
                new_matrix.append(self.get_line(index))

        self.__init__(new_matrix)
        return self

    
    def subtract(self,Li, Lj, ALPHA=1):
        """ Changes destroctively the line Li
                Li = Li - alpha * Lj

            Args:
                Li,Lj -- int -- number of the lines to be swithced
                ALPHA -- int -- constant

            return self
        """
        new_line = list()
        for index in range(self.get_size()['x']):
            new_line.append(self.get_line(Li)[index] - ALPHA * self.get_line(Lj)[index])
        self.change_line(Li, new_line)        

        return self


    def __repr__(self):
        """The representation of the matrix

        return a string
        """
        matrix_print = str()
        for line in range(len(self.matrix['Ax'])):
            for value in self.matrix['Ax'][line]:
                matrix_print += '{:3d}|'.format(value)
            
            matrix_print += '|{:4d}\n'.format(self.matrix['b'][line])
        #Idea for development: Modify the format so it becames flexible
        return matrix_print[:-1]


def clone_matrix(matrix):
    '''Clones the Matrix given as argument

    Args:
        matrix -- Matrix

    returns a Matrix
    '''
    lines = list()

    for i in range(matrix.get_size()['y']):
        lines.append(list(matrix.get_line(i)))

    return Matrix(list(lines))

########
#MATRIX#
########

############################################################################
############################################################################
    
a = [0,1,0,4]

b = [1,0,0,3]

c = [0,1,1,7]

mx = Matrix([a,b,c])
print(mx.get_line_Ax(2))

###############
#TESTING STUFF#
###############

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

