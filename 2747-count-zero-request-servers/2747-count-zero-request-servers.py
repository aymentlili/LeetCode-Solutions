class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        freq = [0] * (n + 1)
        active_cnt = 0
        ans = [0] * len(queries)
        left = 0
        right = 0
        logs_len = len(logs)
        for q_time, q_idx in sorted_queries:
            while right < logs_len and logs[right][1] <= q_time:
                server_id = logs[right][0]
                if freq[server_id] == 0:
                    active_cnt += 1
                freq[server_id] += 1
                right += 1
            limit = q_time - x
            while left < right and logs[left][1] < limit:
                server_id = logs[left][0]
                freq[server_id] -= 1
                if freq[server_id] == 0:
                    active_cnt -= 1
                left += 1
            ans[q_idx] = n - active_cnt
        return ans