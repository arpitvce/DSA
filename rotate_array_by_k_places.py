class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        t=n-k
        temp=[]
        for i in range(t,n):
            temp.append(nums[i])
        for j in range(0,t):
            temp.append(nums[j])
        for i in range(n):
            nums[i]=temp[i]
