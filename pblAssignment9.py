import random

enemyShip = 2 # the enemy ship has two 'health points'. must reach 0 to sink

# a list of all possible outcomes from a cannon firing
cannons = [2,2,1,0] # 1/2 of the outcomes deal two damage (direct hit, enemy ship would have 0 health), 
                    # 1/4 is an indirect hit (need two of these to sink ship), 1/4 is a miss
                    # the elements of this sample space represents these probabilities

winCount = 0 # a win is the ship sinks with the 4 cannon balls
lossCount = 0 # a loss is the enemy ship does not sink with the 4 cannon balls

simulatedRounds = 20000000 # the number of simulations to run

# main simulation loop
for m in range (0,simulatedRounds):

    for i in range(0,4): # loop 4 times to simulate the battle
        index = random.randint(0,len(cannons)-1) # pick a random event, with the probabilities account for
        fire = cannons[index] # the 'damage' to be made to the enemny ship

        enemyShip = enemyShip - fire # apply the damage

    if enemyShip <= 0: # if the enemy ship was sunk in the battle with the 4 cannon balls
        winCount = winCount + 1 # record a win
    else: # if Davy's ship was not sunk in battle
        lossCount = lossCount + 1 # record a loss

    # reset for a new simulation
    enemyShip = 2

result = winCount / simulatedRounds # the result is the number of wins that occured in all the simulations
print("The simulation's result is: ", result)
