class Solution(object):
    def countIslands(self, M, k):
        n = len(M)
        m = len(M[0])
        L = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(n):
            for j in range(m):
                L[i + 1][j + 1] = M[i][j]
        idiv = []
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if L[i][j] > 0:
                    itot = 0
                    queue = [(i, j)]
                    itot += L[i][j]
                    L[i][j] = 0 
                    while queue:
                        r, c = queue.pop()
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if L[nr][nc] > 0:
                                itot += L[nr][nc]
                                L[nr][nc] = 0 
                                queue.append((nr, nc))
                    if itot % k == 0:
                        idiv.append(itot)
        return len(idiv)