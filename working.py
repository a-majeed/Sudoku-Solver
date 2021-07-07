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
    for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i,j) 



