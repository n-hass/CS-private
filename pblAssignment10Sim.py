import random # library for dice rolling

winCount = 0 # the number of winning games
totalRolls = 0 # the total number of rolls across all winning games

"""
Simulates a roll of two dice and returns their sum
"""
def roll(): 
    rollSum = 0
    rollSum = rollSum + random.randint(1,6) # roll the first dice
    rollSum = rollSum + random.randint(1,6) # roll the second dice

    return rollSum


"""
Each run of this function is a simulation of 1 game.
Keeps record of the number of rolls in a game and what each turn was.

Implements logic matching the problem breif, 
with unique rules on the first turn and for subsequent turns.

##  When the game is a win:  ##
Accesses variable 'totalRolls' declared above this function 
to add to the total sum of rolls in all winning games.
returns true

##  When the game is a loss: ##
returns false
"""
def sim():
    global totalRolls
    
    thisGame = [] # the turns (dice roll sums) rollled in this game

    n = 0 # keeps track of number of turns in this game
    refNum = 0 # for tracking the reference number when game takes more than one turn

    while True:
        thisGame.append(roll()) # make the roll and store in list
        
        if n == 0: # if this is the first turn of the game
            if thisGame[n] == 7 or thisGame[n] == 11: # you win if the sum of rolls is 7 or 11
                totalRolls = totalRolls + 1 # sum the number of turns in this game with all other games
                return True
            

            if thisGame[n] == 2 or thisGame[n] == 3 or thisGame[n] == 12: # you lose if sum is 2, 3 or 12
                totalRolls = totalRolls + 1 # sum the number of turns in this game with all other games
                return False
            

            refNum = thisGame[n] # didn't win or lose yet - save the reference number for future turns in this game
        

        if n > 0: # if this is the second or greater turn of the game
            if thisGame[n] == 7: # if you rolled a sum of 7, you lose
                totalRolls = totalRolls + n + 1 # sum the number of turns in this game with all other games
                return False
            
            if thisGame[n] == refNum: # if you rolled your reference number, you win
                totalRolls = totalRolls + n + 1 # sum the number of turns in this game with all other games
                return True
        
        n = n+1 # increment the turn counter


# main loop for simulations
simulatedRounds = 5000000
for m in range(0,simulatedRounds):
    if sim(): # run a simulation
        winCount = winCount + 1 # if it was a win, increment the counter
    
#############################################################################

print("Number of simulations: ",simulatedRounds)
print("Probability of winning: ", (winCount / simulatedRounds) ) # logic: number of wins / number of games played in total. (Real val = 244/495)
print("Avg number of rolls in all games: ", (totalRolls / simulatedRounds) ) # logic: total number of rolls from all games / number of games
