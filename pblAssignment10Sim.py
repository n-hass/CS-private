import random

rollCount = 0
totalRolls = 0

winCount = 0
winRolls = 0


def roll():
    rollSum = 0

    rollSum = rollSum + random.randint(1,6) # roll the first dice

    rollSum = rollSum + random.randint(1,6) # roll the second dice

    return rollSum

def sim():
    global winRolls
    
    thisTurn = []

    n = 0
    refNum = 0

    while True:

        thisTurn.append(roll()) # make the roll and store in array
        
        if n == 0:
            if thisTurn[n] == 7 or thisTurn[n] == 11:
                winRolls = winRolls + n + 1 # add the number of rolls it took to win this game
                return True
            

            if thisTurn[n] == 2 or thisTurn[n] == 3 or thisTurn[n] == 12:
                return False
            

            refNum = thisTurn[n] # save the reference number
        

        if n > 0:
            if thisTurn[n] == 7:
                return False
            
            if thisTurn[n] == refNum:
                winRolls = winRolls + n + 1 # add the number of rolls it took to win this game
                return True
        

        n = n+1 # increment the local turn counter

    

# main loop for simulations
simulatedRounds = 5000000
for m in range(0,simulatedRounds):
    if sim():
        winCount = winCount + 1
    


print("Number of simulations: ",simulatedRounds)
print("probability of winning: ", (winCount / simulatedRounds) ) # 0.4929292929 - 244/495
print("Avg number of rolls to win: ", (winRolls / winCount) )
