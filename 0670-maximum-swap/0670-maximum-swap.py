class Solution:
    def maximumSwap(self, num: int) -> int:
        maxNum=-1
        num=list(str(num))
        replaceWith=replacer=-1
        mappingDict={}
        for n in (range(len(num)-1,-1,-1)):
            if int(num[n])>maxNum:
                maxNum=int(num[n])
                replacer=n
            elif int(num[n])!=maxNum:
                replaceWith=n
                mappingDict[maxNum]=(replacer,replaceWith)
            # else:
        if mappingDict:
            top=max(mappingDict.keys())
            replacer,replaceWith=mappingDict[top]
            num[replacer],num[replaceWith]=num[replaceWith],num[replacer]
        return int("".join(num))