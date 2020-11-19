from concurrent import futures
import time
import concurrent.futures


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
        
        next = int(number // 2)        
        return (next, (step +1) )
    else:
        next = int((number * 3 + 1)  // 2)
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





# num, count = hailstoneStepFast(36,0)


def runCollatzIter(i:int):

    num:int = i
    stepcount = 0
    while num != 1:
        stepAndRes = hailstoneStepFast(num, step=stepcount)
        num = stepAndRes[0]
        stepcount = stepAndRes[1]

    return (i, stepcount)    


# -- fehler results sollten appended sein
starttime = time.time()
with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
    results = [executor.submit(runCollatzIter, i) for i in range(3,500000)]

resDict = {}    
for f in concurrent.futures.as_completed(results):
    singleResTup = f.result()
    print( singleResTup)
    resDict[singleResTup[0]] = singleResTup[1]
  

executor.shutdown()
 # sorted(key_value) returns an iterator over the  
 # Dictionary’s value sorted in keys.   

for i in sorted (resDict) : 
    print ((i, resDict[i]), end ="\n") 
#print(sorted_by_second)  
print('That took {} seconds'.format(time.time() - starttime))






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





#runHailstone(63728127)
# runHailstone(670617279)
# long = runHailstoneFast(63728127)
