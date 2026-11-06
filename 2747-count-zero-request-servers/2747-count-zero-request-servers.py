from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda x: x[1])
        
        # Pair each query with its original index and sort by query time
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0] * len(queries)
        active_servers = {}
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            # Expand the window to include all logs up to time q
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                active_servers[server_id] = active_servers.get(server_id, 0) + 1
                right += 1
                
            # Shrink the window from the left to remove logs older than window_start
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1
                
            # Total servers minus servers that received at least one request
            ans[orig_idx] = n - len(active_servers)
            
        return ans