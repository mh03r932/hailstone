


def hailstoneStep( number:int):
    """
    calculate hailstone
    """
    next: int 
    if number % 2 == 0:
        
        next = int(number / 2)
        
        return next
    else:
        next = number * 3 
        return next + 1
        
    pass

def hailstoneStepFast( number:int, step:int):
    """
    calculate hailstone
    """
    next: int 
    if number % 2 == 0:
        
        next = int(number / 2)        
        return (next, (step +1) )
    else:
        next = int((number * 3 + 1)  / 2)
        return (next, (step + 2))
        
    pass


def runHailstone(num: int, step :int = 1 ):
    """
    docstring
    """
    currentNum = hailstoneStep(number=num)
    print('Step  {:>4}  {:>20}'.format(step, num))
    if(currentNum != 1):
        runHailstone(currentNum, step  +1)
    pass

def runHailstoneFast(num: int, stepcount :int = 1 ):
    """
    docstring
    """

    if(num == 1):
        return stepcount
    else: 
        nextNum, nextStepCount = hailstoneStepFast(number=num, step=stepcount)    
        return runHailstoneFast(nextNum, nextStepCount)
    pass


num, count = hailstoneStepFast(36,0)



# bestum: int = 0
# maxSteps: int = 0 
# for i in range(2, 1000000000 ):
  
#     numOfSteps = runHailstoneFast(i, stepcount=0)    
#     print('n:  {:>4}   {:>20} st'.format(i, numOfSteps))
#     if(maxSteps < numOfSteps):
#         maxSteps = numOfSteps
#         bestum = i
    
#     maxSteps = max(maxSteps, numOfSteps)
# pass

# print ( bestum, ' ',  maxSteps)





runHailstone(63728127)
# runHailstone(670617279)
# long = runHailstoneFast(63728127)
