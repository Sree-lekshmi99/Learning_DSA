class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        pq=[[time,time,1] for time in workerTimes]
        heapq.heapify(pq)
        
        curtime=0
        while mountainHeight:
            time,base,tasks= heapq.heappop(pq)
            curtime=time
            workers=[[time,base,tasks]]

            while pq and pq[0][0]==time:

                timesame,basesame,taskssame= heapq.heappop(pq)
                workers.append([timesame,basesame,taskssame])
            
            for time,base,tasks in workers:
                mountainHeight-=1
                if mountainHeight==0:
                    return curtime

                tasks+=1
                timenext=time+(base*tasks)
                heapq.heappush(pq,[timenext,base,tasks])
    
        return curtime

            