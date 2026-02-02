class Pawn: # moves finished
    def __init__(self,on_board,position,colour):
        self.on_board = on_board
        self.position = position # (x,y)
        self.colour = colour
    
    def possible_moves(self,board):
        if self.on_board:
            move_list = []
            if self.colour == "w" and self.position[0] == 6:
                move_list.append(f"{self.position[0]-1},{self.position[1]}")
                move_list.append(f"{self.position[0]-2},{self.position[1]}")       
            elif self.colour == "b" and self.position[0] == 1:
                move_list.append(f"{self.position[0]+1},{self.position[1]}")
                move_list.append(f"{self.position[0]+2},{self.position[1]}")
            elif self.colour == "w":
                move_list.append(f"{self.position[0]-1},{self.position[1]}")
            elif self.colour == "b":
                move_list.append(f"{self.position[0]+1},{self.position[1]}")
            # an if condition for taking the pieces on the diagonal tiles.

            return move_list
            # add a useless comment
class Rook: # moves finished
    def __init__(self,on_board,position,colour):
        self.on_board = on_board
        self.position = position
        self.colour = colour
    
    def possible_moves(self,board):
        if self.on_board:
            move_list = []

            for u in range(self.position[0], 8):
                if board[u][self.position[1]][5] == "n":
                    move_list.append(f"{u},{self.position[1]}")
                else:
                    break

            for d in range(self.position[0]-1,-1,-1):
                if board[d][self.position[1]][5] == "n":
                    move_list.append(f"{d},{self.position[1]}")
                else:
                    break

            for r in range(self.position[1], 8,1):
                if board[self.position[0]][r][5] == "n":
                    move_list.append(f"{self.position[0]},{r}")
                else:
                    break
            for l in range(self.position[1],-1,-1):
                if board[self.position[0]][l][5] == "n":
                    move_list.append(f"{self.position[0]},{l}")
                else:
                    break
            # returns the move_list with all the possible cells to move
            return move_list
    
class Knight:
    def __init__(self,on_board,position,movement_set,colour):
        self.on_board = on_board
        self.position = position
        self.movement_set = movement_set
        self.colour = colour
    
    def possible_moves(self):
        move_list = []
        # returns the move_list with all the possible cells to move
        return move_list
    
class Bishop:
    def __init__(self,on_board,position,colour):
        self.on_board = on_board
        self.position = position
        self.colour = colour
    
    def possible_moves(self, board): # for debugging
        move_list = []
        fallback_y = self.position[0]
        fallback_x = self.position[1]

        for dr in range(self.position[0], 8):
            try:
                if board[dr][fallback_x+(dr-fallback_y)][5] == "n" and fallback_x+(dr-fallback_y) >= 0:
                    if(dr,fallback_x+(dr-fallback_y)) != self.position:
                        move_list.append(f"{dr},{fallback_x+(dr-fallback_y)}")
                        board[dr][fallback_x+(dr-fallback_y)] = "XXXXX"
                else:
                    break
            except:
                break

        for dl in range(self.position[0],8):
            try:
                print(fallback_x-(dl-fallback_y))
                if board[dl][fallback_x-(dl-fallback_y)][5] == "n" and fallback_x-(dl-fallback_y) >= 0:
                    if (dl,fallback_x-(dl-fallback_y)) != self.position:
                        move_list.append(f"{dl},{fallback_x-(dl-fallback_y)}")
                        board[dl][fallback_x-(dl-fallback_y)] = "XXXXX"
                else:
                    break
            except:
                break

        for ur in range(self.position[0],-1,-1):
            try:
                if board[ur][fallback_x+(ur-fallback_y)][5] == "n" and fallback_x+(ur-fallback_y) >= 0:
                    if (ur,fallback_x+(ur-fallback_y)) != self.position:
                        move_list.append(f"{ur},{fallback_x+(ur-fallback_y)}")
                        board[ur][fallback_x+(ur-fallback_y)] = "XXXXX"
                else:
                    break
            except:
                break
        for ul in range(self.position[0],-1,-1):
            try:
                if board[ul][fallback_x-(ul-fallback_y)][5] == "n" and fallback_x-(ul-fallback_y) >= 0:
                    if (ul,fallback_x-(ul-fallback_y)) != self.position:
                        move_list.append(f"{ul},{fallback_x-(ul-fallback_y)}")
                        board[ul][fallback_x-(ul-fallback_y)] = "XXXXX"

                else:
                    break
            except:
                pass
                

        return move_list,board

class Queen:
    def __init__(self,on_board,position,movement_set,colour):
        self.on_board = on_board
        self.position = position
        self.movement_set = movement_set
        self.colour = colour
    
    def possible_moves(self):
        move_list = []
        # returns the move_list with all the possible cells to move
        return move_list

class King: # moves finished
    def __init__(self,on_board,position,colour,checked):
        self.on_board = on_board
        self.position = position
        self.colour = colour
        self.checked = checked

    def possible_moves(self,board):
        if self.on_board:
            move_list = []

            for y in range(self.position[0]-1, self.position[0]+2, 1):
                for x in range(self.position[1]-1, self.position[1]+2,1):
                    if board[y][x] != board[self.position[0]][self.position[1]]:
                        if board[y][x][5] == "n":
                            move_list.append(f"{y},{x}")
            return move_list
        
    
def Board_set_up(size): # finished
    letters = [chr(i) for i in range(ord('a'), ord('a') + size)]
    numbers = [i+1 for i in range(len(letters))]
    board = [["0" for i in range(size)] for j in range(size)]
    counter = 1

    for i in range(size):
        for j in range(size):
            if counter % 2 == 1:
                board[i][j] = f"{numbers[i]}{letters[j]}-w-n"
            else:
                board[i][j] = f"{numbers[i]}{letters[j]}-b-n"
            counter += 1
        counter += 1

    return board

def Check_check(king_pos, possible_moves):
    # function that will check if a king is checked
    return

def Mate_check(checked, possible_moves):
    # function that checks whether a king is mated
    return 

def move(self):
    # returns either the board with the new position of the piece,
    # or the coordinates of the point, where the piece is to move
    return


board = Board_set_up(8)

board = [['1a-w-n', '1b-b-n', '1c-w-n', '1d-b-n', '1e-w-n', '1f-b-n', '1g-w-n', '1h-b-n'], 
         ['2a-b-n', '2b-w-n', '2c-b-n', '2d-w-n', '2e-b-n', '2f-w-n', '2g-b-n', '2h-w-n'], 
         ['3a-w-n', '3b-b-n', '3c-w-n', '3d-b-n', '3e-w-n', '3f-b-n', '3g-w-n', '3h-b-n'], 
         ['4a-b-n', '4b-w-n', '4c-b-n', '4d-w-n', '4e-b-n', '4f-w-n', '4g-b-o', '4h-w-n'], 
         ['5a-w-n', '5b-b-n', '5c-w-n', '5d-b-n', '5e-w-n', '5f-b-n', '5g-w-n', '5h-b-n'], 
         ['6a-b-n', '6b-w-n', '6c-b-n', '6d-w-n', '6e-b-n', '6f-w-n', '6g-b-n', '6h-w-n'], 
         ['7a-w-n', '7b-b-n', '7c-w-n', '7d-b-n', '7e-w-n', '7f-b-n', '7g-w-n', '7h-b-n'], 
         ['8a-b-n', '8b-w-n', '8c-b-n', '8d-w-n', '8e-b-n', '8f-w-n', '8g-b-n', '8h-w-n']]

Bishop1 = Bishop(True, (4,3),"w")
move_list,board = Bishop1.possible_moves(board)
print(move_list)
print()

for i in range(len(board)):
    print(board[i])
