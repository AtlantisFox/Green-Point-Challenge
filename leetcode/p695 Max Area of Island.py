"""
裸广搜
"""

class Solution:

    f = None
    d = ((0, -1), (0, 1), (-1, 0), (1, 0))
    n = 0
    m = 0

    def bfs(self, grid, i, j):
        queue = [(i, j)]
        self.f[i][j] = True
        ans = 1
        while len(queue) != 0:
            now = queue.pop(0)
            for k in range(4):
                x = now[0] + self.d[k][0]
                y = now[1] + self.d[k][1]
                if 0 <= x < self.n and 0 <= y < self.m and grid[x][y] == 1 and self.f[x][y] == False:
                    queue.append((x, y))
                    self.f[x][y] = True
                    ans += 1
                    
        return ans

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.n = len(grid)
        self.m = len(grid[0])
        self.f = [[False] * self.m] * self.n
        self.f = [[False for i in range(self.m)] for j in range(self.n)]

        ans = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.f[i][j] == False and grid[i][j] == 1:
                    ans = max(ans, self.bfs(grid,i,j))
        return ans


if __name__ == '__main__':
    map = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    # map = [[0,0,0,0,0,0,0,0]]

    s = Solution()
    print(s.maxAreaOfIsland(map))

    # print(s.n, s.m)
