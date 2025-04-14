# Any problem can be converted to a priority Queue 
# Egs :   4 jobs are runing 
# Queue = [Job1, Job2  ]  # Not Job 2 and Job 1 as 1 is high priority 
# Only Jon van run > 

# . When Job Came > 
#     Queue Insert 
#     put top Queue running

#  Next Job Came :
#     Queue Insert 
#     check if job running :
#         if yes : wait 
#             else: put top queue to run 
#  Next event is job finish :
#     free the run 
#     put the Fits Priority Job to run 

import heapq

class PQueue:
    def __init__(self,queue=None):
        if queue is None:
            self.Q1=[]
        else:
            self.Q1=queue
        self.jobrunning=0
     
    def put_job_to_run(self):
        if self.Q1:
           if self.jobrunning==0:
            self.jobrunning+=1
            print(f'Executing currently {self.Q1[0]=} {self.jobrunning=}')
           else:
            print(f'Job running now , stay in Queue {self.Q1=}')
           return 
        else:
           print(f'Empty Queue')

    def InsertJobToQueue(self,Job):

        if Job[1]=='Start':
            # finding Job priority felf
            priority=JobsMap[Job[0]]
            heapq.heappush(self.Q1,(priority,Job))
        else:
            heapq.heappop(self.Q1)
            self.jobrunning-=1     
    
JobsMap= {'Job1':1,'Job2':2,'Job3':3,'Job4':4}
Input=[['Job1','Start'],
       ['Job3','Start'],
       ['Job2','Start'],
       ['Job1', 'End']]


Day1 = PQueue()

for Jobsequence in Input:
    Day1.InsertJobToQueue(Jobsequence)
    Day1.put_job_to_run()
print(f'Day 1 Queue Looks like {Day1.Q1=}')