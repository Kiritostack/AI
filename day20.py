def runningSum(self, nums):
        sum=0
        result=[]
        for num in nums:
            sum=sum+num
            result.append(sum)
        return result    