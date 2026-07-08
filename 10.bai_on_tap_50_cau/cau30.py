from collections import deque

def round_robin_scheduling(processes, burst_time, quantum):
    n = len(processes)
    queue = deque(range(n))
    rem_bt = list(burst_time)
    wt = [0] * n
    tat = [0] * n
    completion_time = [0] * n
    
    t = 0
    while queue:
        i = queue.popleft()
        if rem_bt[i] > quantum:
            t += quantum
            rem_bt[i] -= quantum
            queue.append(i)
        else:
            t += rem_bt[i]
            wt[i] = t - burst_time[i]
            rem_bt[i] = 0
            completion_time[i] = t
            
    return completion_time

processes = [1, 2, 3]
burst_time = [5, 2, 4]
quantum = 2
print(round_robin_scheduling(processes, burst_time, quantum))