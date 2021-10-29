board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#addasd
def valid (board, num, pos):

    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    boxX = pos[1] //3
    boxY = pos[0] //3

    for i in range(boxY*3, boxY*3+3):
        for j in range(boxX*3, boxX*3+3):
           if board[i][j] == num and (i,j) != pos:
               return False


    return True

def solve(board):

    findEmpty = isEmpty(board);

    if not findEmpty:
        return True
    else:
        row, col = findEmpty

        for i in range(1, 10):
            if valid (board, i, (row, col)):
                board[row][col] = i

                if (solve(board)):
                    return True;
                else:
                    board[row][col] = 0

        return False



def printBoard(b):
    for i in range(len(b)):
        if i != 0 and i % 3 == 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def isEmpty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)

    return None;

