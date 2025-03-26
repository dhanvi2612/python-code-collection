original_grid = [_ for _ in range(0,9)]
grid = [_ for _ in range(0,9)]
displayedgrid=[" " for _ in range(0,9)]

    #printing the grid
def display_grid(agrid):
    for a in range(0,9):
        if (a)%3==0:
            print("\n|",end="")
        print(agrid[a]," ",end="|")
    print()

    #defining the 2 players's characteristics
class Player():
    def __init__(self,letter,name):
        self.letter=letter
        self.name=name

    def __str__(self):
        return f"Player is {self.name} playing with {self.letter}"

    #initialising the players with user input
def definingplayers():
    global a,b
    a=Player("X",input("Player 1: Playing with 'X': Enter name: "))
    b=Player("O",input("Player 2: Playing with 'O': Enter name: "))

def comparing(x,y,z):
    if x==y==z:
        return True

    #tic_winner conditions
#tic_winner conditions
def win(grid,player):
    global tic_winner,tic_loser
        #creating a new list where each column is a nested list
    p,q,r=[_ for _ in grid[0:3]],[_ for _ in grid[3:6]],[_ for _ in grid[6:]]
    newlist=[p,q,r]

        #checking rows
    for j in newlist:
        if comparing(j[0],j[1],j[2]):
            tic_winner=player
            return f"{player} has won the game!"

        #checking columms
    for k in range(0,3):
        if comparing(newlist[0][k],newlist[1][k],newlist[2][k]):
            tic_winner=player
            return f"{player} has won the game!"

        #checking diagonals
    if comparing(grid[0],grid[4],grid[8]) or comparing(grid[2],grid[4],grid[6]):
        tic_winner=player
        return f"{player} has won the game!"

        #checking tie
    for z in range(0,9):
        if grid[z]==original_grid[z]:
            break
    else:
        tic_winner=tic_loser=None
        return f"It's a tie! No one won!"

    return False


    #checking if the user's move is valid:
def validatingmove(move):
    try:
        movie=int(move) #input should be int
        if movie>8 or movie<0: #input should be in the range 0-8
            raise ValueError
        if grid[movie] not in original_grid: #input should not be 'x' or 'o'
            raise ValueError
    except ValueError:
        print("Invalid Move")
        return False
    else:
        return True

def playingplayer(player):
    global winner
    display_grid(displayedgrid)

    while True:
        move=input(f"Player {player.name}'s (playing {player.letter}) turn! Play (0-8): ")
        if validatingmove(move):
            break
    move=int(move)

        #adding to the grid
    grid[move]=player.letter
    displayedgrid[move]=player.letter
    print(f"{player.name} has placed an {player.letter} at {move}!")

        #checking for win
    winner=win(grid,player.name)
    return win(grid,player.name)

    #playing the game
def play():
    definingplayers() #a and b
    print("\nHere's your official grid: ",end="") #printing grid
    display_grid(original_grid)

    while True:
        if not playingplayer(a) and not playingplayer(b):
           continue
        else:
            print("\n**********")
            print(f"{winner.upper()}") #printing result of the game
            print("**********\nThe winning board: ",end="")
            display_grid(displayedgrid)
            break

if __name__ == "__main__":
    play()