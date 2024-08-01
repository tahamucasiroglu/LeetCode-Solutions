# 213. House Robber II && Difficult Easy


# tek çift sıra mantığında gittiğim [1,3,1,3,100] dizisi ile patladığım çözüm
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             return max(nums[0], nums[1])
#         even = odd = 0
#         for i,n in enumerate(nums):
#             if i % 2 == 0:
#                 even += n
#             else:
#                 odd += n
#         if len(nums) % 2 == 1:
#             return max(odd, even - min(nums[0], nums[-1]))
#         return max(even,odd)



# ikinci adım başarısız çok uzadı
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         return max(self.process(nums,0), self.process(nums,1), self.process(nums,2), self.process(nums,3))
    
#     def process(self, nums: list[int], lower:int) -> int:
#         if len(nums) <= 3:
#             return max(nums)
#         result = 0
#         if lower > 0:
#             for i in range(lower):
#                 nums[nums.index(max(nums))] = 0
#         while True:
#             maxNum = max(nums)
#             result += maxNum
#             index = nums.index(maxNum)
#             if index == 0:
#                 nums = nums[2:-1]
#             elif index == len(nums) - 1:
#                 nums = nums[1:-2]
#             else:
#                 nums = nums[0:index-1] + nums[index+2:]
#             if len(nums) <= 3:
#                 return result + max(nums)






# gpt çıktısı
# def rob(nums):
#     def rob_line(houses):
#         n = len(houses)
#         if n == 0:
#             return 0
#         if n == 1:
#             return houses[0]
#         dp = [0] * n
#         dp[0] = houses[0]
#         dp[1] = max(houses[0], houses[1])
#         for i in range(2, n):
#             dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
#         return dp[-1]
    
#     if not nums:
#         return 0
#     if len(nums) == 1:
#         return nums[0]
    
#     return max(rob_line(nums[:-1]), rob_line(nums[1:]))

# # Örnek dizi
# nums = [6, 6, 4, 8, 4, 3, 3, 10]
# print(rob(nums))  # Çıktı: 27



# gpt + leetcode çözümleri + ben
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         if len(nums) <= 3: 
#             return max(nums)
#         lenNums = len(nums) - 1
#         res1 = [0] * lenNums
#         res2 = [0] * lenNums
#         res1[0] = nums[0]
#         res1[1] = max(nums[0],nums[1])
#         res2[0] = nums[1]
#         res2[1] = max(nums[1], nums[2])
#         for i in range(2,lenNums):
#             res1[i] = max(res1[i-1], res1[i-2] + nums[i])
#             res2[i] = max(res2[i-1], res2[i-2] + nums[i+1])
#         return max(res1[-1], res2[-1])




# yeni bakış açısı
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         lenNums = len(nums) - 1
#         if lenNums <= 2: 
#             return max(nums)
#         res1_1 = 0
#         res1_2 = 0
#         res1_3 = 0
#         res2_1 = 0
#         res2_2 = 0
#         res2_3 = 0
#         res1_1 = nums[0]
#         res1_2 = max(nums[0],nums[1])
#         res2_1 = nums[1]
#         res2_2 = max(nums[1], nums[2])
#         for i in range(2,lenNums):
#             res1_3 = max(res1_2, res1_1 + nums[i])
#             res2_3 = max(res2_2, res2_1 + nums[i+1])
#             res1_1, res1_2 = res1_2, res1_3
#             res2_1, res2_2 = res2_2, res2_3
#         return max(res1_3, res2_3)

class Solution:
    def rob(self, nums: list[int]) -> int:
        lenNums = len(nums) - 1
        if lenNums <= 2: 
            return max(nums)
        res1_1 = nums[0]
        res2_1 = nums[1]
        res1_2 = max(res1_1,nums[1])
        res2_2 = max(res2_1, nums[2])
        for i in range(2,lenNums):
            res1_1, res1_2 = res1_2, max(res1_2, res1_1 + nums[i])
            res2_1, res2_2 = res2_2, max(res2_2, res2_1 + nums[i+1])
        return max(res1_2, res2_2)





if __name__ == "__main__":
    testArray = [
        [[2,3,2], 3],
        [[1,2,3,1], 4],
        [[1,2,3], 3],
        [[1], 1],
        [[1,3,1,3,100], 103],
        [[200,3,140,20,10], 340],
        [[1,7,9,4], 11],
        [[6,6,4,8,4,3,3,10],27],
        [[1,2,3,4,5,1,2,3,4,5], 16]
    ]

    sol = Solution()

    for i,n in enumerate(testArray):
        res = sol.rob(n[0])
        print(f"Test {i+1} "+ ("Başarılı " if res == n[1] else "Başarısız ") + f" res = {res}   expect = {n[1]}")

