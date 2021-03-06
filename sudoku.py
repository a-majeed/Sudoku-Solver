board = [
    [9,0,0,0,0,0,0,0,0],
    [3,0,0,0,6,0,0,2,0],
    [0,0,5,0,0,0,7,0,3],
    [0,3,1,0,8,4,0,0,0],
    [8,2,0,0,1,0,5,4,9],
    [0,4,0,0,0,0,8,0,0],
    [7,5,0,1,0,6,0,8,0],
    [4,0,0,8,0,0,1,0,0],
    [0,0,0,7,0,0,0,0,0]
]


def display_board(bo):

    """
    displays the board
    :param bo: 2d List of ints
    :return: None
    """

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!= 0:
                print (" | ", end="")

            if j == 8:
                print(bo[i][j])
            
            else:
                print(str(bo[i][j]) + " ", end="")



def find_available(bo):

    """
    finds an empty space (empty spaces set as 0) in the board
    :param bo: incomplete board
    :return: (int, int) row col
    """
    
    for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i,j) 
    
    return None


def valid(bo, num, pos):

    """
    Returns if inputted number attempt is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    #checking rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #checking columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(3*box_y, 3*box_y +3):
        for j in range(3*box_x, 3*box_x +3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def solver(bo):

    """
    Solves the sudoku board 
    :param bo: 2d list of ints
    :return: solution
    """

    finder = find_available(bo)

    if not finder:
        return True
    else:
        row, column = finder
    
    for i in range(1,10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i

            if solver(bo):
                return True

            bo[row][column] = 0

solver(board)
display_board(board)
    