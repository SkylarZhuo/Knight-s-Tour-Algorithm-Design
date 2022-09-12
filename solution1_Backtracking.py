
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
        '''
        Constructor -- create new instances of board.
        Parameters: 
        self -- the current object.
        size -- an integer, the size of the board.
        board -- a 2-d array represents the states of the board, 0 means not visited, other 
                 positive integers represent the visiting order.
        start_pos -- an array of two elements representing the starting point of the knight.
        directions -- a 2-D array represents the eight directions the kight can move. 
        '''                       
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
        moves = [[x + y for x,y in zip(cur_pos,direction)] for direction in self.directions]  #get the positions after possible moves 
        valid_moves = [move for move in moves if 0<=move[0]<self.BDsize                       #check if the move is inside the boarder
                        and 0<=move[1]<self.BDsize                 
                        and self.board[move[0]][move[1]] == 0]                                #check if the move is landing on an empty square.
        return valid_moves
    
    def searchNext(self, cur_pos, moveCount):  
        '''
        Method -- searchNext
        Parameters:
            self -- the current object.
            cur_pos -- the current position of the knight.
            moveCount -- the current steps the knight has taken.
        Purpose: search the next step recursively until find a solution 
        Return: return true if there exist a solution, return false if no solution
        ''' 
        #add one of the next moves to solution the route
        self.board[cur_pos[0]][cur_pos[1]] = moveCount
        #if find a complete route return true     
        if moveCount >= self.BDsize* self.BDsize:
            return True
            
        moves = self.findMoves(cur_pos)
        if len(moves) == 0 :  
            return False
    
        for move in moves:
            #recursively check if the current move leads to a legal move.                
            if self.searchNext(move, moveCount + 1):    
                return True
            #if the move above doesn't lead to a leagal move then remove this move
            #from our route and try other alternative moves.
            else:
                self.board[move[0]][move[1]] = 0
   

    def tour(self):
        '''
        Method -- tour
        Parameters:
            self -- the current object.
        Purpose: starting the process of tour from given point.
        Return: return ture if the tour is finished; return false if no complete tour.
        '''
        cur_pos = self.start_pos
        self.board[cur_pos[0]][cur_pos[1]] = 1                #number the starting point to step 1 in the route
        return self.searchNext(cur_pos, 1)                    #start to search for the next step  
        
    def printPath(self):
        '''
        Method -- printPath
        Parameters:
            self -- the current object.
        Purpose: print the complete path.
        Return: none
        '''
        print("---------------------------------------")
        for row in self.board:
            for column in row:
                print(column, end='\t')
            print("")
        print("---------------------------------------")

def main():    
    KT = KnightTour(8, [0,0])      
    if KT.tour(): 
        KT.printPath()
    else: 
        print("No route")
        
if __name__ == "__main__":
    main()