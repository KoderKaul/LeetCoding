class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjMatrix = [[float('inf')] * n for _ in range(n)]
        
        # Set the distance from a city to itself to 0
        for i in range(n):
            adjMatrix[i][i] = 0

        for u,v,wt in edges:
            adjMatrix[u][v]=wt
            adjMatrix[v][u]=wt
        for stop in range(n):
            for i in range(n):
                for j in range(n):
                    stopDist= adjMatrix[i][stop] + adjMatrix[stop][j]
                    if stopDist <= distanceThreshold:
                        adjMatrix[i][j]=min(adjMatrix[i][j],  stopDist)
        # print(adjMatrix)
        smallest=float('inf')
        index=0
        for i in range(n):
            tempSmall=0
            for j in range(n):
                if adjMatrix[i][j]!=float("inf") and adjMatrix[i][j]<=distanceThreshold:
                    tempSmall+=1
            if tempSmall<=smallest:
                smallest=tempSmall
                index=i
        return index
