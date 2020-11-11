

import math
from typing import *
import time
from concurrent.futures import ProcessPoolExecutor, as_completed



def collatz_step_fast( number:int, step:int) -> Tuple[int, int]:
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



def run_collatzer_iter(i:int)-> Tuple[int, int]:

    num:int = i
    stepcount = 0
    while num != 1:
        stepAndRes = collatz_step_fast(num, step=stepcount)
        num = stepAndRes[0]
        stepcount = stepAndRes[1]

    return (i, stepcount)    

def run_collatzer_for_list(nums) -> Dict[int, int]:
    return {n: run_collatzer_iter(n)[1] for n in nums}


def trigger_collatz_search(nums, nprocs: int):

    starttime = time.time()

    size_of_workgroup = int(math.ceil(len(nums) / nprocs))
    futures = []

    with ProcessPoolExecutor(max_workers=8) as executor:

        for i in range (nprocs):
           workgroup = nums[(i * size_of_workgroup) : ((i + 1) * size_of_workgroup)] 
           futures.append(executor.submit(run_collatzer_for_list, workgroup))

    merged_result = {}
    for f in as_completed(futures):
        workjob_res_dict = f.result()    
    #    print( workjob_res_dict)
        merged_result.update(workjob_res_dict)

    for i in sorted (merged_result) : 
        print ((i, merged_result[i]), end ="\n") 
    #print(sorted_by_second)  
    print('That took {} seconds'.format(time.time() - starttime))

    return merged_result

trigger_collatz_search(range(3,63728127), 4)

#runHailstone(63728127)
# runHailstone(670617279)
# long = runHailstoneFast(63728127)
