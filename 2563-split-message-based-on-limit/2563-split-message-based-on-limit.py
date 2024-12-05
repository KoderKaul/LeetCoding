class Solution(object):
    def splitMessage(self, message, limit):
        """
        :type message: str
        :type limit: int
        :rtype: List[str]
        """
        a=0
        n = len(message)

        for k in range(1, n+1):
            a+=len(str(k))
            b = len(str(k))*k
            common = 3*k

            if limit*k - (a+b+common) >= n:
                res = []
                i = 0

                for j in range(1, k+1):
                    suffix = f'<{j}/{k}>'
                    mes = message[i:i+limit-len(suffix)] + suffix
                    res.append(mes)
                    i+=(limit-len(suffix))
                return res
        return []






        
        