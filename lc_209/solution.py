from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        r = 0
        result = float("inf")
        
        #sliding window algorithm 
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                result = min(result, (r-l+1))
                total -= nums[l]
                l += 1

        return 0 if result == float("inf") else result 

def main():
    sol = Solution()
    result = sol.minSubArrayLen(target=11, nums=[1,2,3,4,5])
    print(result)

if __name__ == "__main__":
    main()
