'''
CS5800 Final project
Summer 2022
Ce(Lydia) Zhao,
Yingying Feng,
Zhuohang(Skylar) Li,
Zheng Gong
Knight Tour 
This a project given a N*N board with the knight placed on a given starting position,
and the knight should move according to the rules of must visit each square exactly once.
If there exist a route that satify the rule, we print the order of each cell in which they
are visited.
'''

class KnightTour:
    '''
    Class KnightTour
    Attributes: BDsize, board, start_pos, directions
    Methods: findMoves, searchNext, tour, printPath 
    '''
  
    def __init__(self, size, s_pos):          
        self.BDsize = size                                        
        self.board = [[0]* size for _ in range(size )]       
        self.start_pos = s_pos                
        self.directions = [[2,1],[2,-1],[-2,1],[-2,-1],    
                        [1,2],[1,-2],[-1,2],[-1,-2]]

    
    def findMoves(self, cur_pos):
        '''
        Method -- findMoves
        Parameters:
            self -- the current object.
            cur_pos -- the current position of the knight.
        Purpose: search the valid moves of the knight according to the current position.
        Return: a 2-d array including all possible valid moves of the knight.
        '''
        #Get the list of positions after moves to eight directions.
        moves = [[x + y for x,y in zip(cur_pos,direction)] for direction in self.directions]  
        #check if the move is inside the boarder.
        valid_moves = [move for move in moves if 0<=move[0]<self.BDsize
                        and 0<=move[1]<self.BDsize
                        #check if it moves towards to an empty square.
                        and self.board[move[0]][move[1]] == 0]
        return valid_moves

    def tour(self):
        '''
        Method -- tour
        Parameters:
            self -- the current object.
        Purpose: starting the process of tour from given point.
        Return: return ture if the tour is finished; return false if no complete tour.
        '''
        cur_pos = self.start_pos
        #number the starting point to step 1 in the route
        self.board[cur_pos[0]][cur_pos[1]] = 1
        return self.searchNext(cur_pos, 1)      #start to search for the next step  

    def printPath(self):
        '''
        Method -- printPath
        Parameters:
            self -- the current object.
        Purpose: print the complete path.
        Return: none
        '''
        print("-------------------------")
        for row in self.board:
            for column in row:
                print(column, end='\t')
            print("")
        print("-------------------------")
        
         
    def countNext(self, cur_pos):
        '''
        Method -- countNext
        Parameters:
            self -- the current object.
            cur_pos --  the current position of the knight.
        Purpose: count the number of valid moves from the given position.
        Return: an integer indicates the number of valid moves.
        '''
        valid_moves = self.findMoves(cur_pos)
        return len(valid_moves)
    
    def countDegree(self, cur_pos):
        '''
        Method -- countDegree
        Parameters:
            self -- the current object.
            cur_pos --  the current position of the knight.
        Purpose: get all valid moves with their corresponding degrees. The degree is the number of valid moves
                 for the given postiotion.
        Return: a 3-D array like [[2, [2,3]], [3, [1,4]]], for each element, the first item 
                indicates the number of valid moves corresponding to the position given by the second item.
        '''
        valid_moves = self.findMoves(cur_pos)
        return [[self.countNext(move),move] for move in valid_moves]

    def searchNext(self, cur_pos, moveCount):
        '''
        Method -- searchNext
        Parameters:
            self -- the current object.
            cur_pos -- the current position of the knight.
            moveCount -- the current steps the knight has taken.
        Purpose:  search the next step recursively until find a complete path. If there are 
                  multiple valid moves, choose the move with minimum degree(accessibility).
        Return: return true if there exist a solution, return false if no solution
        '''
        #add one of the next moves to the route
        self.board[cur_pos[0]][cur_pos[1]] = moveCount   
        if moveCount >= self.BDsize* self.BDsize:
            return True
        else:
            #Here moves is 3D-array like [[2, [2,3]], [3, [1,4]]]
            moves = self.countDegree(cur_pos)
            #Sort the array so that the posisition with minimum degree is at the first place.
            moves.sort()
            #This statement is to determing if we arrive at a dead point "D" where one of its next
            #move "M" has 0 valid next move. It means that to arrive point "M" we must go through
            #point "D". If "D" is not the next to last move, we could never find a path going through "M".
            if moves[0][0] == 0 and moveCount!= self.BDsize*self.BDsize -1:
                return False
            for move in moves:
                #recursively check if the current move leads to a legal move.                
                if self.searchNext(move[1], moveCount+1):
                    return True
                #if the move above doesn't lead to a leagal move then remove this move
                #from our route and try other alternative moves.
                else :
                    self.board[cur_pos[0]][cur_pos[1]] = 0
def main():
    while True:
        try:
            BDsize = int(input("Please enter a board size less than 32: "))
            r = int(input("Please enter a row number of the start point: "))
            c = int(input("Please enter a column number of the start point: "))   
            if r < 0 or r > BDsize or c < 0 or c > BDsize:     
                print("Invalid input")   
                continue
            else:
                startPoint = [r, c]
                break 
            
        except ValueError:
            print("Invalid input")              
                
    KT = KnightTour(BDsize, startPoint)       
    if KT.tour():                  
        KT.printPath()   
    else:
        print("No route exists!\n")
    
    
                
        
    
if __name__ == "__main__":
    main()