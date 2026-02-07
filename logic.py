
# task list
# 1. conditions for the casting to be approved to the move_list
# 2. взятие на проходе
# 3. taking for all the pieces                                       ---- done
# 4. check                                                           ---- done
# 5. mate                                                            ---- done
# 6. promotion of the pawn, fix the pawn generally

# need to fix the fact that you can take the king --- fixed
# need to rewrite move functions so that the pieces can protect each other, therefore the king wouldn't be able to take protected pieces 
#   /|\
#    | 
#  fixed
#
# need to find a way to unflag the cells

# dictionary
# rooks: WRA, WRH, BRA, BRH
# knights: WKB, WKG, BKB, BKG
# bishops: WBC, WBF, BBC, BBF
# queens: WQQ, BQQ
# kings: WKK, BKK
# pawns: WPA, WPB, WPC, WPD, WPE, WPF, WPG, WPH
#        BPA, BPB, BPC, BPD, BPE, BPF, BPG, BPH

# board[i][j] = nnn-w-?-? = "Name-colour_of_the_cell-attacked_by_white-attacked_by_black"
# nnn-w-0-1 means that the cell is NOT attacked by white, but is attacked by black

BLACK_UP = False

class Piece:
    def __init__(self,on_board,position,name):
        self.on_board = on_board
        self.position = position # (y,x) the index
        self.ever_moved = False
        self.name = name

    def possible_moves_pawn(self,board): # works, but no en passant

        if self.on_board:
            move_list = []
            if BLACK_UP:
                print(self.name[0])
                if self.name[0] == "W":
                    if self.position[0] == 6:
                        move_list.append(f"{self.position[0]-1},{self.position[1]}") # does not work, there is not such thing as self.colour
                        move_list.append(f"{self.position[0]-2},{self.position[1]}")
                        board[self.position[0]-1][self.position[1]-1] = board[self.position[0]-1][self.position[1]-1][:6] + '1' + board[self.position[0]-1][self.position[1]-1][7:]
                        board[self.position[0]-1][self.position[1]+1] = board[self.position[0]-1][self.position[1]+1][:6] + '1' + board[self.position[0]-1][self.position[1]+1][7:]

                    else:
                        move_list.append(f"{self.position[0]-1},{self.position[1]}") 
                        board[self.position[0]-1][self.position[1]-1] = board[self.position[0]-1][self.position[1]-1][:6] + '1' + board[self.position[0]-1][self.position[1]-1][7:]
                        board[self.position[0]-1][self.position[1]+1] = board[self.position[0]-1][self.position[1]+1][:6] + '1' + board[self.position[0]-1][self.position[1]+1][7:]

                else:
                    if self.position[0] == 1:
                        move_list.append(f"{self.position[0]+1},{self.position[1]}")
                        move_list.append(f"{self.position[0]+2},{self.position[1]}")
                        board[self.position[0]+1][self.position[1]-1] = board[self.position[0]+1][self.position[1]-1][:8] + '1'
                        board[self.position[0]+1][self.position[1]+1] = board[self.position[0]+1][self.position[1]+1][:8] + '1'

                    else:
                        move_list.append(f"{self.position[0]+1},{self.position[1]}")
                        board[self.position[0]+1][self.position[1]-1] = board[self.position[0]+1][self.position[1]-1][:8] + '1'
                        board[self.position[0]+1][self.position[1]+1] = board[self.position[0]+1][self.position[1]+1][:8] + '1'

            else:
                if self.name[0] == "W":
                    if self.position[0] == 1:
                        move_list.append(f"{self.position[0]+1},{self.position[1]}")
                        move_list.append(f"{self.position[0]+2},{self.position[1]}")
                        board[self.position[0]+1][self.position[1]-1] = board[self.position[0]+1][self.position[1]-1][:6] + '1' + board[self.position[0]+1][self.position[1]-1][7:]
                        board[self.position[0]+1][self.position[1]+1] = board[self.position[0]+1][self.position[1]+1][:6] + '1' + board[self.position[0]+1][self.position[1]+1][7:]

                    else:
                        move_list.append(f"{self.position[0]+1},{self.position[1]}") 
                        board[self.position[0]+1][self.position[1]-1] = board[self.position[0]+1][self.position[1]-1][:6] + '1' + board[self.position[0]+1][self.position[1]-1][7:]
                        board[self.position[0]+1][self.position[1]+1] = board[self.position[0]+1][self.position[1]+1][:6] + '1' + board[self.position[0]+1][self.position[1]+1][7:]


                else:
                    if self.position[0] == 6:
                        move_list.append(f"{self.position[0]-1},{self.position[1]}")
                        move_list.append(f"{self.position[0]-2},{self.position[1]}")
                        board[self.position[0]-1][self.position[1]-1] = board[self.position[0]+1][self.position[1]-1][:8] + '1'
                        board[self.position[0]-1][self.position[1]+1] = board[self.position[0]+1][self.position[1]+1][:8] + '1'

                    else:
                        move_list.append(f"{self.position[0]-1},{self.position[1]}")
                        board[self.position[0]-1][self.position[1]-1] = board[self.position[0]+1][self.position[1]-1][:8] + '1'
                        board[self.position[0]-1][self.position[1]+1] = board[self.position[0]+1][self.position[1]+1][:8] + '1'

            # an if condition for taking the pieces on the diagonal tiles.

            return move_list,board
    def possible_moves_rook(self,board): # works completely
        if self.on_board:
            move_list = []

            for u in range(self.position[0], 8):
                if (u,self.position[1]) != self.position:
                    if board[u][self.position[1]][2] == "K":
                        break
                    if board[u][self.position[1]][0] != self.name[0]:    
                        move_list.append(f"{u},{self.position[1]}")

                    if self.name[0] == 'W':
                        board[u][self.position[1]] = board[u][self.position[1]][:6] + "1" + board[u][self.position[1]][7:]
                    else:
                        board[u][self.position[1]] = board[u][self.position[1]][:8] + "1"

                    if board[u][self.position[1]][0] != "n":
                        break



            for d in range(self.position[0]-1,-1,-1):
                
                if (d,self.position[1]) != self.position: 
                    if board[d][self.position[1]][2] == "K":
                        break
                    if board[d][self.position[1]][0] != self.name[0]:
                        move_list.append(f"{d},{self.position[1]}")
                
                    if self.name[0] == "W":
                        board[d][self.position[1]] = board[d][self.position[1]][:6] + '1' + board[d][self.position[1]][7:]
                    else:
                        board[d][self.position[1]] = board[d][self.position[1]][:8] + '1' 


                    if board[d][self.position[1]][0] != "n":
                        break


            for r in range(self.position[1], 8,1):
                
                if (self.position[0],r) != self.position:
                    if board[self.position[0]][r][2] == "K":
                        break
                    if board[self.position[0]][r][0] != self.name[0]:
                        move_list.append(f"{self.position[0]},{r}")
                
                    if self.name[0] == "W":
                        board[self.position[0]][r] = board[self.position[0]][r][:6] + '1' + board[self.position[0]][r][7:]
                    else: 
                        board[self.position[0]][r] = board[self.position[0]][r][:8] + '1'

                    if board[self.position[0]][r][0] != "n":
                        break


            for l in range(self.position[1],-1,-1):
                    
                if (self.position[0],l) != self.position: 
                    if board[self.position[0]][l][2] == "K":
                        break
                    if board[self.position[0]][l][0] != self.name[0]:
                        move_list.append(f"{self.position[0]},{l}")
                    
                    if self.name == "W":
                        board[self.position[0]][l] = board[self.position[0]][l][:6] + '1' + board[self.position[0]][l][7:]
                    else:
                        board[self.position[0]][l] = board[self.position[0]][l][:8] + "1"
                    
                    if board[self.position[0]][l][0] != "n":
                        break

            # returns the move_list with all the possible cells to move
            return move_list,board
    def possible_moves_knight(self,board): # works completely
        move_list = []
        potential_move_list = [f"{self.position[0]-1},{self.position[1]+2}",
                               f"{self.position[0]+1},{self.position[1]+2}",
                               f"{self.position[0]-1},{self.position[1]-2}",
                               f"{self.position[0]+1},{self.position[1]-2}",
                               f"{self.position[0]+2},{self.position[1]+1}",
                               f"{self.position[0]+2},{self.position[1]-1}",
                               f"{self.position[0]-2},{self.position[1]+1}",
                               f"{self.position[0]-2},{self.position[1]-1}"]
        for i in range(len(potential_move_list)):
            try:
                if board[int(potential_move_list[i][0])][int(potential_move_list[i][2])][2] != "K":
                
                    if self.name[0] == "W":
                        board[int(potential_move_list[i][0])][int(potential_move_list[i][2])] = board[int(potential_move_list[i][0])][int(potential_move_list[i][2])][:6] + '1' + board[int(potential_move_list[i][0])][int(potential_move_list[i][2])][7:]
                    else:
                        board[int(potential_move_list[i][0])][int(potential_move_list[i][2])] = board[int(potential_move_list[i][0])][int(potential_move_list[i][2])][:8] + '1'

                    if board[int(potential_move_list[i][0])][int(potential_move_list[i][2])][0] != self.name[0]:
                        move_list.append(potential_move_list[i])
            except:
                pass

        

        return move_list, board    
    def possible_moves_bishop(self,board): # works completely
        if self.on_board:
            move_list = []
            fallback_y = self.position[0]
            fallback_x = self.position[1]

            for dr in range(self.position[0], 8):
                try:
                    if fallback_x+(dr-fallback_y) >= 0:

                        if(dr,fallback_x+(dr-fallback_y)) != self.position and board[dr][fallback_x+(dr-fallback_y)][2] != "K":
                            if board[dr][fallback_x+(dr-fallback_y)][0] != self.name[0]:
                                move_list.append(f"{dr},{fallback_x+(dr-fallback_y)}")


                            if self.name[0] == "W":
                                board[dr][fallback_x+(dr-fallback_y)] = board[dr][fallback_x+(dr-fallback_y)][:6] + "1"+ board[dr][fallback_x+(dr-fallback_y)][7:]
                            else:
                                board[dr][fallback_x+(dr-fallback_y)] = board[dr][fallback_x+(dr-fallback_y)][:8] + "1"
                            

                            if board[dr][fallback_x+(dr-fallback_y)][0] != "n":
                                break

                    else:
                        break
                except:
                    break

            for dl in range(self.position[0],8):
                try:
                    print(fallback_x-(dl-fallback_y))
                    if fallback_x-(dl-fallback_y) >= 0:

                        if (dl,fallback_x-(dl-fallback_y)) != self.position and board[dl][fallback_x-(dl-fallback_y)][2] != "K":

                            if board[dl][fallback_x-(dl-fallback_y)][0] != self.name[0]:
                                move_list.append(f"{dl},{fallback_x-(dl-fallback_y)}")


                            if self.name[0] == "W":
                                board[dl][fallback_x-(dl-fallback_y)] = board[dl][fallback_x-(dl-fallback_y)][:6] + "1" + board[dl][fallback_x-(dl-fallback_y)][7:]
                            else:
                                board[dl][fallback_x-(dl-fallback_y)] = board[dl][fallback_x-(dl-fallback_y)][:8] + "1"

                            if board[dl][fallback_x-(dl-fallback_y)][0] != "n":
                                break

                    else:
                        break
                except:
                    break

            for ur in range(self.position[0],-1,-1):
                try:
                    if fallback_x+(ur-fallback_y) >= 0:
                        if (ur,fallback_x+(ur-fallback_y)) != self.position and board[ur][fallback_x+(ur-fallback_y)][2] != "K":


                            if board[ur][fallback_x+(ur-fallback_y)][0] != self.name[0]:
                                move_list.append(f"{ur},{fallback_x+(ur-fallback_y)}")


                            if self.name[0] == "W":
                                board[ur][fallback_x+(ur-fallback_y)] = board[ur][fallback_x+(ur-fallback_y)][:6] + "1" + board[ur][fallback_x+(ur-fallback_y)][7:]
                            else:
                                board[ur][fallback_x+(ur-fallback_y)] = board[ur][fallback_x+(ur-fallback_y)][:8] + "1"

                            if board[ur][fallback_x+(ur-fallback_y)][0] != "n":
                                break
                    else:
                        break
                except:
                    break
            for ul in range(self.position[0],-1,-1):
                try:
                    if fallback_x-(ul-fallback_y) >= 0:
                        if (ul,fallback_x-(ul-fallback_y)) != self.position and board[ul][fallback_x-(ul-fallback_y)][2] != "K":
                        


                            if board[ul][fallback_x-(ul-fallback_y)][0] != self.name[0]:
                                move_list.append(f"{ul},{fallback_x-(ul-fallback_y)}")


                            if self.name[0] == "W":
                                board[ul][fallback_x-(ul-fallback_y)] = board[ul][fallback_x-(ul-fallback_y)][:6] + "1" + board[ul][fallback_x-(ul-fallback_y)][7:]
                            else:
                                board[ul][fallback_x-(ul-fallback_y)] = board[ul][fallback_x-(ul-fallback_y)][:8] + "1"

                            if board[ul][fallback_x-(ul-fallback_y)][0] != "n":
                                break
                    else:
                        break
                except:
                    pass
                    

            return move_list,board
    def possible_moves_king(self, board): # momves and takes with caution, no castling though
        if self.on_board:
            move_list = []

            for y in range(self.position[0]-1, self.position[0]+2, 1):
                for x in range(self.position[1]-1, self.position[1]+2,1):
                    
                    if (y,x) != self.position:
                        try:
                            if board[y][x][0] != self.name[0]: # so that the king can take the pieces

                                if self.name[0] == "W":
                                    if board[y][x][8] != "1" and board[y][x][2] != "K": # if the piecce is unprotected, the move is added to the move_list
                                        move_list.append(f"{y},{x}")
                                        board[y][x] = board[y][x][:6] + "1"+ board[y][x][7:]

                                else:
                                    if board[y][x][6] != "1" and board[y][x][2] != "K":
                                        move_list.append(f"{y},{x}")
                                        board[y][x] = board[y][x][:8] + "1"
                        except:
                            pass

            # the castling logic must be here
                            
            return move_list, board
        

    def Move_n_Take(self,new_coords,board,Pieces): # not debugged

        if self.name[1:2] == "KK" and self.ever_moved == False and (new_coords == (7,6) or new_coords == (0,6)):
            board = self.short_castling()
        elif self.name[1:2] == "KK" and self.ever_moved == False and (new_coords == (7,2) or new_coords == (0,2)):
            board = self.long_castling()
        else:
            # the taking infrastructure
            Cell_content =  board[new_coords[0]][new_coords[1]][:2] # find what stood on the cell previously
            board[new_coords[0]][new_coords[1]].replace(Cell_content, self.name) # put a new piece on the cell
           
            self.ever_moved = True

            if Cell_content != "nnn":
                for i in range(0,len(Pieces)):
                    if Cell_content == Pieces[i].name: # find the piece that was taken in the pieces list
                        Cell_content = Pieces[i]
                    
                self.Find_yourself(Cell_content, board) # put the pieces on new coords on the board
            self.Find_yourself(board)


        return board
    def Find_yourself(self,board): # not debugged
        # if you can't find yourself on the board, then you're off the board
        old_coordinates = self.position
        for i in range(0,len(board),1):
            for j in range(0,len(board),1):
                if board[i][j][:3] == self.name:
                    self.position = (i,j)

        if old_coordinates == self.position:
            self.on_board = False
            self.position = None
    

class Pawn(Piece): # moves finished, need to solve the promoted issue

    def possible_moves(self,board):
        return self.possible_moves_pawn(board) # returns only the move_list
class Rook(Piece): # moves finished

    def possible_moves(self,board):
        return self.possible_moves_rook(board)# returns the move_list and the board
class Knight(Piece): # moves finished
    
    def possible_moves(self,board):
        return self.possible_moves_knight(board) # returns both the board and the move_list
class Bishop(Piece): # moves finished
    def possible_moves(self, board):
        return self.possible_moves_bishop(board) # returns the board too
class Queen(Piece): # moves finished
    def possible_moves(self,board):
        move_list1, b = self.possible_moves_bishop(board)
        move_list2, b = self.possible_moves_rook(board)

        actual_move_list = []

        for i in range(len(move_list1)):
            actual_move_list.append(move_list1[i])
        for i in range(len(move_list2)):
            actual_move_list.append(move_list2[i])
        return actual_move_list
class King(Piece): # moves finished
    def possible_moves(self,board):
        return self.possible_moves_king(board)
    def short_castling(self,new_coords, board): # not debugged
        if new_coords == (7,6):
                board[7][6] = board[7][6].replace("nnn",self.name)
                board[7][5] = board[7][5].replace("nnn",f"{self.name[0]}RH")
                self.ever_moved = True

        elif new_coords == (0,6):
                board[0][6] = board[0][6].replace("nnn",self.name)
                board[0][5] = board[0][5].replace("nnn",f"{self.name[0]}RH")
                self.ever_moved = True # the pieces need to find themselves
        return board
    def long_castling(self,new_coords, board, Pieces): # not debugged

        if new_coords == (7,2):
                board[7][2] = board[7][2].replace("nnn",self.name)
                board[7][3] = board[7][3].replace("nnn",f"{self.name[0]}RH")
                self.ever_moved = True

        elif new_coords == (0,2):
                board[0][2] = board[0][2].replace("nnn",self.name)
                board[0][3] = board[0][3].replace("nnn",f"{self.name[0]}RH")
                self.ever_moved = True # the pieces need to find themselves
        
        rook_name = f"{self.name[0]}RH"
        for i in range(0,len(Pieces)):
            if  rook_name == Pieces[i].name: # find the piece that was taken in the pieces list
                rook_name = Pieces[i]
        
        self.Find_yourself(rook_name,board) # for the rook
        self.Find_yourself(board) # for the king

        return board
    def Checked(self, board): # works
        if self.name[0] == "W":
            if board[self.position[0]][self.position[1]][8] == "1":
                return True
        else:
            if board[self.position[0]][self.position[1]][6] == "1":
                return True
        
        # function that will check if a king is checked
        return False
    def Mated(self,board): # works
        move_list,board = self.possible_moves(board)
        if len(move_list) == 0:
            return True
        else:
            return False

def Board_set_up(size,black_up): # finished
    List =  ["WRA", "WKB", "WBC", "WQQ", "WKK", "WBF", "WKG", "WRH", "WPA", "WPB", "WPC", "WPD", "WPE", "WPF", "WPG", "WPH"]
    List2 = ["BRA", "BKB", "BBC", "BQQ", "BKK", "BBF", "BKG", "BRH", "BPA", "BPB", "BPC", "BPD", "BPE", "BPF", "BPG", "BPH"]

    board = [["0" for i in range(size)] for j in range(size)]
    counter = 1

    for i in range(size):
        counter += 1
        for j in range(size):
                counter += 1
            
                if black_up:
                    if i == 0:
                        if counter % 2 == 1:
                            board[i][j] = f"{List2[j]}-w-?-?"
                        else:
                            board[i][j] = f"{List2[j]}-b-?-?"
                    elif i == 1:
                        if counter % 2 == 1:
                            board[i][j] = f"{List2[j+8]}-w-?-?"
                        else:
                            board[i][j] = f"{List2[j+8]}-b-?-?"
                    elif i == 6:
                        if counter % 2 == 1:
                            board[i][j] = f"{List[j+8]}-w-?-?"
                        else:
                            board[i][j] = f"{List[j+8]}-b-?-?"
                    elif i == 7:
                        if counter % 2 == 1:
                            board[i][j] = f"{List[j]}-w-?-?"
                        else:
                            board[i][j] = f"{List[j]}-b-?-?"
                    else:
                        if counter % 2 == 1:
                             board[i][j] = f"nnn-w-?-?"
                        else:
                            board[i][j] = f"nnn-b-?-?"
                    
                else:
                    if i == 0:
                        if counter % 2 == 1:
                            board[i][j] = f"{List[j]}-w-?-?"
                        else:
                            board[i][j] = f"{List[j]}-b-?-?"
                    elif i == 1:
                        if counter % 2 == 1:
                            board[i][j] = f"{List[j+8]}-w-?-?"
                        else:
                            board[i][j] = f"{List[j+8]}-b-?-?"
                    elif i == 6:
                        if counter % 2 == 1:
                            board[i][j] = f"{List2[j+8]}-w-?-?"
                        else:
                            board[i][j] = f"{List2[j+8]}-b-?-?"
                    elif i == 7:
                        if counter % 2 == 1:
                            board[i][j] = f"{List2[j]}-w-?-?"
                        else:
                            board[i][j] = f"{List2[j]}-b-?-?"
                    else:
                        if counter % 2 == 1:
                             board[i][j] = f"nnn-w-?-?"
                        else:
                            board[i][j] = f"nnn-b-?-?"
                    
    return board

    # function that checks whether a king is mated
    return 
def Create_Pieces(): # finished
    WRA = Rook(True, (0,7),"WRA")
    WRH = Rook(True, (7,7),"WRH")
    BRA = Rook(True, (0,0),"BRA")
    BRH = Rook(True, (7,0),"BRH")

    WKB = Knight(True, (1,7),"WKB")
    WKG = Knight(True, (6,7),"WKG")
    BKB = Knight(True, (1,0),"BKB")
    BKG = Knight(True, (6,0),"BKG")

    WBC = Bishop(True, (2,7),"WBC")
    WBF = Bishop(True, (5,7),"WBF")
    BBC = Bishop(True, (2,0),"BBC")
    BBF = Bishop(True, (5,0),"BBF")

    WQQ = Queen(True, (3,7),"WQQ")
    BQQ = Queen(True, (3,0),"BQQ")

    WKK = King(True, (4,7),"WKK")
    BKK = King(True, (4,0),"BKK")

    WPA = Pawn(True, (0,1),"WPA")
    WPB = Pawn(True, (1,1),"WPB")
    WPC = Pawn(True, (2,1),"WPC")
    WPD = Pawn(True, (3,1),"WPD")
    WPE = Pawn(True, (4,1),"WPE")
    WPF = Pawn(True, (5,1),"WPF")
    WPG = Pawn(True, (6,1),"WPG")
    WPH = Pawn(True, (7,1),"WPH")

    BPA = Pawn(True, (0,1),"BPA")
    BPB = Pawn(True, (1,1),"BPB")
    BPC = Pawn(True, (2,1),"BPC")
    BPD = Pawn(True, (3,1),'BPD')
    BPE = Pawn(True, (4,1),"BPE")
    BPF = Pawn(True, (5,1),"BPF")
    BPG = Pawn(True, (6,1),'BPG')
    BPH = Pawn(True, (7,1),"BPH")

    return WRA, WRH, BRA, BRH, WKB, WKG, BKB, BKG, WBC, WBF, BBC, BBF, WQQ, BQQ, WKK, BKK, WPA, WPB, WPC, WPD, WPE, WPF, WPG, WPH, BPA, BPB, BPC, BPD, BPE, BPF, BPG, BPH

'''
board = Board_set_up(8, True)
Pieces = []
Pieces = Create_Pieces()

board = [['BRA-w-?-?', 'BKB-b-?-?', 'BBC-w-?-?', 'BQQ-b-?-?', 'BKK-w-?-?', 'BBF-b-?-?', 'BKG-w-?-?', 'BRH-b-?-?'],
         ['BPA-b-?-?', 'BPB-w-?-?', 'BPC-b-?-?', 'BPD-w-?-?', 'BPE-b-?-?', 'BPF-w-?-?', 'BPG-b-?-?', 'BPH-w-?-?'],
         ['nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?'],
         ['nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?'],
         ['nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?'],
         ['nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?', 'nnn-b-?-?', 'nnn-w-?-?'],
         ['WPA-w-?-?', 'WPB-b-?-?', 'WPC-w-?-?', 'WPD-b-?-?', 'WPE-w-?-?', 'WPF-b-?-?', 'WPG-w-?-?', 'WPH-b-?-?'],
         ['WRA-b-?-?', 'WRH-w-?-?', 'WKB-b-?-?', 'WKG-w-?-?', 'WBC-b-?-?', 'WBF-w-?-?', 'WQQ-b-?-?', 'WKK-w-?-?']]

WBC = Pawn(True, (6,4),"BKK")
move_list,board = WBC.possible_moves(board)
print(move_list)

for i in range(len(board)):
    print(board[i])
'''


# allow for multiple boards by turning the coords from the init into a list
# to see whether the action is a take, compare the coordinates from the move_list with the coordinates of the board, and 
# if the cell is not empty, draw the thingie