import random 

maxAttempts = 100 #stops the program after 100 attempts
count = 9999
solCount = 0

while count > maxAttempts:
    solCount +=1
    # init array
    puzzle = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(0)
            #print row
        puzzle.append(row)

    #for r in puzzle:
    #    print(r)

    # get random value
    for row in range(9):
        for col in range(9):
            thisRow=puzzle[row]
            thisCol=[]
            for h in range(9):
                thisCol.append(puzzle[row][col])

            subCol = int(col/3)
            subRow = int(row/3)
            subMat = []
            for subR in range (3):
                for subC in range (3):
                    subMat.append(puzzle[subRow*3 + subR][subCol*3 + subC])
            randVal = 0
            count = 0
            while randVal in thisRow or randVal in thisCol or randVal in subMat:
                randVal = random.randint(1,9)
                count+=1

                if count > maxAttempts: break 
            puzzle[row][col] = randVal

            if count > maxAttempts: break 

        if count > maxAttempts:
            break


for r in puzzle: print(r)
