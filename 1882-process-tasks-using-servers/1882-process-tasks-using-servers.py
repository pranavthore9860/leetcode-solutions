import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        
        # Min-heap of available servers: (weight, index)
        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)
        
        # Min-heap of busy servers: (free_time, weight, index)
        unavailable = []
        
        ans = [0] * m
        curr_time = 0
        
        for j in range(m):
            curr_time = max(curr_time, j)
            
            # If no servers are available, jump time to when the next server frees up
            if not available and unavailable:
                curr_time = max(curr_time, unavailable[0][0])
            
            # Release all servers that become free at or before curr_time
            while unavailable and unavailable[0][0] <= curr_time:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            # Assign the task to the highest-priority available server
            weight, index = heapq.heappop(available)
            ans[j] = index
            
            # Push the server into the unavailable heap with its new release time
            heapq.heappush(unavailable, (curr_time + tasks[j], weight, index))
            
        return ans