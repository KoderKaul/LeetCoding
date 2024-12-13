class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        s_arr=[(-1,float("inf"))]*n
        s=[]
        for i in range(n-1,-1,-1):
            # find the next greatest element
            while s and s[-1][0]>nums[i]:
                top,ii = s.pop()
                if top < s_arr[i][-1]:
                    s_arr[i]=(ii,top)
            s.append((nums[i],i))
        
        for index in range(n-1,-1,-1):
            i=s_arr[index][0]
            if i != -1:
                #the rightmost index that can be swapped
                nums[i],nums[index]=nums[index],nums[i]
                #remaining should be sorted so that we get the smallest permutation
                t = sorted(nums[index+1:])
                for i in range(index+1, n):
                    nums[i]=t[i-index-1]
                break
        else:
            nums.sort()