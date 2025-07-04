class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[float('inf') for _ in range(n+1)]
        dp[n]=0
        dp[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i]=min(dp[i+1], dp[i+2])+nums[i]
        # print(dp)
        return min(dp[0], dp[1])
        