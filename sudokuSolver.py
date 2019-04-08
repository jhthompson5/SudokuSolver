numSet = [1,2,3,4,5,6,7,8,9]
import copy
def deductive(puzzle):    
    """Initialize set of possible values for every index in puzzle"""
    solved = []
    posSet = []  
    for lineIndex,line in enumerate(puzzle):
        solved.append(False)
        posSet.append([])
        for i in line:
            posSet[lineIndex].append([1,2,3,4,5,6,7,8,9])
    counter = 0
    changed = True
    """set limit for testing""" 
    while(changed == True): 
        last = copy.deepcopy(posSet)
        posSet = getPossibilities(puzzle,posSet)
        if last == posSet:
            changed = False
        puzzle = updatePuzzle(puzzle,posSet)
    return puzzle,posSet
    
    
def getPossibilities(puzzle,posSet):
    for lineIndex,line in enumerate(puzzle):
        for rowIndex,val in enumerate(line):
            if val != 0:
                posSet[lineIndex][rowIndex] = [val]
            else:
                #Check Box
                boxLineIndex = lineIndex % 3
                boxRowIndex = rowIndex % 3
                boxRange = [[lineIndex - boxLineIndex, lineIndex + (2-boxLineIndex)],
                [rowIndex - boxRowIndex, rowIndex + (2-boxRowIndex)]]
                for y in range(boxRange[0][0],boxRange[0][1]+1):
                    for x in range(boxRange[1][0],boxRange[1][1]+1):
                        checkVal = puzzle[y][x]
                        if checkVal != 0:
                            if checkVal in posSet[lineIndex][rowIndex]:
                                posSet[lineIndex][rowIndex].remove(checkVal)
                    
                
                #Check Line
                y = lineIndex
                for x in range(9):
                    checkVal = puzzle[y][x]
                    if checkVal != 0:
                        if checkVal in posSet[lineIndex][rowIndex]:
                            posSet[lineIndex][rowIndex].remove(checkVal)
                
                #Check Column
                x = rowIndex
                for y in range(9):
                    checkVal = puzzle[y][x]
                    if checkVal != 0:
                        if checkVal in posSet[lineIndex][rowIndex]:
                            posSet[lineIndex][rowIndex].remove(checkVal)
                          
    return posSet

def updatePuzzle(puzzle,posSet):
    for lineIndex,line in enumerate(puzzle):
        for rowIndex,val in enumerate(line):
            if val == 0:
                if len(posSet[lineIndex][rowIndex]) == 1:
                    puzzle[lineIndex][rowIndex] = posSet[lineIndex][rowIndex][0]
    return puzzle


def solve(board):
    board,posSet = deductive(board)
    
    y = 0
    x = 0

    posSet = init(board,posSet)

    add = True
    while y < 9:
        while x < 9 and x > -1:
            if len(posSet[y][x]) > 1:
                success = False #board[y][x] != 0 and checkRow(board,x,y) and checkCol(board,x,y) and checkBox(board,x,y) 
                index = posSet[y][x].index(board[y][x])+1
                while success == False and index < len(posSet[y][x]):       
                    board[y][x] = posSet[y][x][index]
                    success = checkRow(board,x,y) and checkCol(board,x,y) and checkBox(board,x,y)
                    index += 1
                if success:
                    add = True
                    x += 1
                else:
                    add = False
                    board[y][x] = posSet[y][x][0]
                    x -= 1
            else:
                if add:
                    x += 1
                else:
                    x -= 1
                
        if add:
            x = 0
            y += 1
        else:
            x = 8
            y -= 1
            
    return board    

def init(board,posSet): #Set all values on board to the first index in posSet
    for y in range(0,9):
        for x in range(0,9):
            if len(posSet[y][x])>1: 
                temp = posSet[y][x].copy()           
                posSet[y][x] = [0]
                for i in temp:
                    posSet[y][x].append(i)
    return posSet
                

def checkRow(board,rowInd,colInd):
    val = board[colInd][rowInd]
    for x in range(0, 9):
        if x!=rowInd:
            if board[colInd][x] == val:
                return False
    return True
    
def checkCol(board,rowInd,colInd):
    val = board[colInd][rowInd]
    for y in range(0, 9):
        if y!=colInd:
            if board[y][rowInd] == val:
                return False
    return True
    
def checkBox(board,rowInd,colInd):
    boxRowStart = rowInd - rowInd % 3
    boxColStart = colInd - colInd % 3
    boxRowEnd = 2 - (rowInd % 3) + rowInd
    boxColEnd = 2 - (colInd % 3) + colInd
    
    val = board[colInd][rowInd]
    
    for x in range(boxRowStart, boxRowEnd+1):
        for y in range(boxColStart,boxColEnd+1):
            if x!=rowInd or y!=colInd:
                if board[y][x] == val:
                    return False
    return True
    
problem = [[0,0,1,0,0,7,0,0,4],
 [0,5,0,0,4,0,0,1,0],
 [4,0,0,5,0,0,9,0,0],
 [1,0,0,2,0,0,6,0,0],
 [0,4,0,0,8,0,0,2,0],
 [0,0,6,0,0,9,0,0,3],
 [0,0,7,0,0,8,0,0,6],
 [0,6,0,0,1,0,0,4,0],
 [5,0,0,9,0,0,3,0,0]]

#solution = [[9, 2, 6, 5, 8, 3, 4, 7, 1], [7, 1, 3, 4, 2, 6, 9, 8, 5], [8, 4, 5, 9, 7, 1, 3, 6, 2], [3, 6, 2, 8, 5, 7, 1, 4, 9], [4, 7, 1, 2, 6, 9, 5, 3, 8], [5, 9, 8, 3, 1, 4, 7, 2, 6], [6, 5, 7, 1, 3, 8, 2, 9, 4], [2, 8, 4, 7, 9, 5, 6, 1, 3], [1, 3, 9, 6, 4, 2, 8, 5, 7]]

ret = solve(problem)
print(ret)
#if ret == solution:
#    print("YAY")