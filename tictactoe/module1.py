

def main(): 
    board = [["None","O","X"],
             ["None", "X","O"],
             ["X","O","X"]]

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
            print(winner)
            return winner
    match = []



    ##loop vertical
    for i in range(3):
        #   loop indices of row
        for row in board: #gets the lists of board

            match.append(row[i]) #get current index of board 

        if if_match(match): #if true return
            winner = match[0]
            print( winner)
            return
        match = []
    
    #flatten board and check diagonals
    flat = [cell for row in board for cell in row] #mkaes a flat list of the board

    match = [flat[0], flat[4], flat[8]] #diagonal 1
    if if_match(match):
        winner = match[0]
        print( winner)
        return winner

    match = [flat[2], flat[4], flat[6]] #diagonal 2
    if if_match(match):
        winner = match[0]
        print( winner)
        return winner

    return None #return None if no winner found
    



if __name__ == "__main__":
    main()

