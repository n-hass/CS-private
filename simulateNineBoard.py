import random

def validate(current):
    n = len(current) -1

    test = False
    
    if n == 7:
        up = current[7]+current[4]
        left = current[7]+current[6]
        if up%2==0 or left%2==0:
            test = True
    
    if n == 6:
        up = current[6]+current[3]
        if up%2==0:
            test = True
    
    if n == 5:
        up = current[5] + current[2]
        left = current[5]+current[4]
        if up%2==0 or left%2==0:
            test = True
    
    if n == 4:
        up = current[4]+current[1]
        left = current[4]+current[3]
        if up%2==0 or left%2==0:
            test = True

    if n == 3:
        up = current[3] + current[0]
        if up%2==0:
            test = True

    if n == 2:
        left = current[2] + current[1]
        if left%2==0:
            test = True

    if n == 1:
        left = current[1] + current[0]
        if left%2==0:
            test = True

    if n == 0:
        test = False        

    return test                        

    

## start of main ##

#init
graySum = 0
graySumIndex = 0
whiteSum = 0
base = [1,2,3,4,5,6,7,8,9]

mainRecord = []

current = []
holding = []

#main loop
for m in range(0,362880): #362880

    valid = True # reset the table valididy tracker for each new table

    for i in range(0,9):
        
        # pick a random number as an index of base, place the value in the next position in current and remove it from base
        index = random.randint(0,len(base)-1)
        current.append( base.pop(index) )

        
        if i<8:
            while validate(current): # loop while validation fails. chooses new random number from base, appends it to current and checks validity again

                holding.append( current.pop(i) ) # place number into a holding array if it fails and remove from current

                if len(base) == 0:
                    valid = False
                    base.extend(holding)
                    break
                
                index = random.randint(0,len(base)-1) # get another random index of base
                current.append( base.pop(index) ) # append the random num from base to current
        elif i == 8:
            up = current[8] + current[5]
            left = current[8] + current[7]
            if up%2==0 or left%2==0:
                valid = False # test if this last value was valid. if not, set valid tracker to False
        
        if len(holding) > 0 and valid:
            #holding.pop( holding.index(current[i]) ) # once passed, remove the successful number from the holding array 
            base.extend(holding) # and put all numbers in the holding array back in to base

        holding = []

        if not valid:
            break
    
    mainRecord.append([current])

    if valid:
        newGraySum = current[2]+current[3]+current[4]+current[8]

        if graySum < newGraySum:
            graySum = newGraySum
            whiteSum = current[0]+current[1]+current[5]+current[6]+current[7]
            graySumIndex = m
    
    # re-init for next loop iteration
    current = []
    base = [1,2,3,4,5,6,7,8,9]

print("\nwinning table:")
print(mainRecord[graySumIndex])
print("Gray sum:")
print(graySum)
print("White sum:")
print(whiteSum) 
print("")
