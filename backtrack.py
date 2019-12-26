
def print_board(board):
    for i in range(9): 
        if i % 3 == 0 and i != 0: #this is divide out each of the sudoku squares, chop by column 3
            print("- - - - - - - - - - -")
        for j in range(9): 
            if j % 3 == 0 and j != 0: # this is to print out the separators
                print("| ", end="")
            
            if j == 8: #this is if it is the last element of the boad, 
                print(board[i][j]) #print without a space inbetween and add newline
            else:
                print(str(board[i][j]) + " ", end="") #print out the element with a space, dont newline 

#make a mode where the user can put in the numbers themselves
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if(board[r][c] == 0): #check if the board has an empty space
                return (r,c) #return both row and column
    return None #if nothing is empty, then return nothing
    
def solver(board):
    #take a board a try to fill it
    pos= find_empty(board)
    if pos:
        row, col = pos
    else:
        return True #return true if board is already solved
    
    #use backtracking in order to solve board
    for i in range(1,10): #from 1-9 
        if checker(board,pos,i):
            board[row][col] = i

            if solver(board):
                return True
            
            board[row][col] = 0 #if checker fails, change the pos back to 0

def checker(board,pos,num):
    row,col = pos
    #checks the row
    for j in range(9): #checks for repeat in row
        if board[row][j] == num and col != j:
            return False
    #check the column
    for i in range(9):
        if board[i][col] == num and col != i: #checks for repeat in column
            return False

    #check the surrounding box
    box_x = row//3 
    box_y = col//3
    for i in range(3*box_x, 3*box_x + 3):
        for j in range(3*box_y, 3*box_y + 3):
            if board[i][j] == num and (i,j) != pos: #if theres another number in the box that isnt at the position
                return False
    
    return True

if __name__ == "__main__":

    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
    print_board(board)
    print()
    if (solver(board)):
        print_board(board)
    else:
        print("No solution exists")
