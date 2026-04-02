class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input array of intervals
        #What we do to the input -> merge overlapping intervals
        #Return list of non-overlapping intervals that covers all intervals in the input
        
        #Intervals are non-overlapping if they have no common point
        #Example -> [1,2] and [3,4] are non-overlapping
        # [1,2] and [2,3]

        #We want the range basically of values 
        #Example ->  [1,3] in the range [1,5] we want the bigger range
        #Return [[1,5], [6,7]] We merge the ones with overlap

        #Example [[1,2], [2,3]]
        #Output is [1,3] Because we take the largest range, 1 and 3 
        
        #we'll have a result array that we need to return 
        
        #sort through the intervals 
        #O(logn)
        #sort by the start value 
        intervals.sort(key = lambda pair : pair[0])

        #input the first interval to avoid the edge case 
        output = [intervals[0]]

        #go through each interval
        for start, end in intervals:
            #get most recent and end value 
            lastEnd = output[-1][1]

            if start <= lastEnd:
                #overlap
                #merge the intervals
                #[1,5], [2,4] -> [1,5]
                output[-1][1] = max(lastEnd, end)
            else:
                #take the interval and add it to the output if it's not overlapping 
                output.append([start,end])

        return output 

