"""
Tic Tac Toe Player
"""

import math
import copy
from collections import Counter as c

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): #count how many X's and O's are on the board, with X being the first player
    """
    Returns player who has the next turn on a board.
    Flatten the board to a single list, then count the number of X's and O's using Counter
    """
    # Count the number of X's and O's on the board
    #flatten list: we want the cell that is in the row x of the whole board
    #get cell from row list from the board nested list, we want the index cell that is in the row list
    flat_board = [cell for row in board for cell in row] 

    count = c(flat_board) #initalized count; we gave count module the list to read from
    #count X
    x = count[X]
    #count O
    o = count[O]

    if x > o:
        return O
    else: return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    
    """
    possible_actions = set() #initialize an empty set to store possible actions

    for row in range(len(board)): #takes length of the board, and gives the index of the row(three in this case)
        for cell in range(len(board[row])): #takes row of board (now just a list), get len then iterate range (3 this case)
            if board[row][cell] == EMPTY:
                possible_actions.add((row, cell)) #add the cell to the set of possible actions

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    have to do a deep copy so that we don't modify the original board
    """
    #action tuple (r,c) into indexes for the board
    row, cell = action #unpack the tuple into row and cell
    
    #copy board
    board_copy = copy.deepcopy(board) #copies all elemeents
    if board_copy[row][cell] != EMPTY:
        raise ValueError("Error: Cell is already occupied") #if the cell is not empty, raise an error
    board_copy[row][cell] = player(board) #put X or O depending on the current player to the specified cell

    return board_copy  #return the new board with the move made 
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    match = []
    winner = None

    ##########################################################
    def if_match(mylist):
        #check if any of them None
        if None in mylist:
            return False
        return all(i == mylist[0] for i in mylist)
    ##########################################################
    
    #loop horizontal
    for row in board:
        if if_match(row):
            winner = row[0]
            #print(winner)
            return winner
    match = []



    ##loop vertical
    for i in range(3):
        #   loop indices of row
        for row in board: #gets the lists of board

            match.append(row[i]) #get current index of board 

        if if_match(match): #if true return
            winner = match[0]
            #print( winner)
            return winner
        match = []
    
    #flatten board and check diagonals
    flat = [cell for row in board for cell in row] #mkaes a flat list of the board

    match = [flat[0], flat[4], flat[8]] #diagonal 1
    if if_match(match):
        winner = match[0]
        #print( winner)
        return winner

    match = [flat[2], flat[4], flat[6]] #diagonal 2
    if if_match(match):
        winner = match[0]
        #print( winner)
        return winner

    return None #return None if no winner found


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    if all(cell for row in board for cell in row):
        return True

    return False  # Game is not over if no winner and there are still empty cells

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)

    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #check if game is over
    if terminal(board):
        return None  # No action possible if the game is over

    
    #X turn
    if player(board)=="X":
        _, move = max_value(board, -math.inf, math.inf) 
    #O turn
    else:
        _, move = min_value(board, -math.inf, math.inf)
    #_ is being used by max/min_value as a hold value of the move value, we don't need it here

    return move  # Return the best move found by minimax


#max value
def max_value(board, alpha, beta):
    "returns the **highest value of move and the move itself"
    #check if game has eneded
    if terminal(board):
        return utility(board), None  # Return utility value and no move

    v = -math.inf # Initialize v to negative infinity
    best_move = None  # Initialize best move

    for action in actions(board):
        #get move of O if player X makes this action
        min_result, _ = min_value(result(board, action), alpha, beta) #gives tuple but dont care for tohers
        if min_result > v:
            v = min_result
            best_move = action

        #prune: the biggest value min will give max
        alpha = max(alpha, v)
        if alpha >= beta:
            break

    return v, best_move

#min value
def min_value(board, alpha, beta):
    "returns the **lowest value of move and the move itself"
    if terminal(board):
        return utility(board), None
    
    v = math.inf  # Initialize v to positive infinity
    best_move= None  # Initialize best move

    for action in actions(board):
        max_result, _ = max_value(result(board, action), alpha, beta)
        if max_result < v:
            v = max_result
            best_move = action

    #prune : the lowest value max will give min
        beta = min(beta, v)
        if beta <= alpha:
            break

    return v, best_move  # Return the lowest value and the best move found
