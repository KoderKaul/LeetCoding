class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def tangent(x,y):
            if y[0]-x[0] == 0:
                return 1e8
            return (y[-1]-x[-1])/float(y[0]-x[0])
        n = len(points)
        if n<3:
            return n
        maxlen=1
        for index,pt in enumerate(points):
            tangents={}
            for i2,pt2 in enumerate(points[index+1:]):
                # if index != i2:
                tan = tangent(pt2,pt)
                if tan in tangents:
                    tangents[tan]+=1
                else:
                    tangents[tan]=1

                maxlen=max(maxlen,tangents[tan])
                    # if tan in tangents:
                    #     tangents[tan][index].append(i2)
                    #     # maxlen=max(maxlen,len(tangents[tan][index]))
                    # else:
                    #     tangents[tan]=[[] for _ in points]
                    #     tangents[tan][index] = [i2]
                    #     # maxlen=max(maxlen,len(tangents[tan][index]))
        # for values in tangents.values():
        #     # temp=0
        #     for i in values:
        #         maxlen=max(maxlen,len(i))

        return maxlen+1