class Solution(object):
    def canFinish(self, numCourses, prereq):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList={}
        parents=[0 for i in range(numCourses)]
        for course, pre in prereq:
            if pre not in adjList:
                adjList[pre]=[]
            adjList[pre].append(course)
            parents[course]+=1
        queue = []
        for i,c in enumerate(parents):
            if c == 0:
                queue.append(i)
        order=0
        # listy=[]
        while queue:
            pre = queue.pop(0)
            if pre in adjList:
                for course in adjList[pre]:
                    parents[course]-=1
                    if parents[course]==0:
                        queue.append(course)
            # parents[pre] = -1
            # listy.append(pre)
            order+=1
        # print(listy)
        return order == numCourses
        