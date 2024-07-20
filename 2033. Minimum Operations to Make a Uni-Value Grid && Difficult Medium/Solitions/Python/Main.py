#kendi çözümüm biraz uzun ama anlaşılır ve hızlı diyebilirim tabi aslında en yavaşı kalmakta fakat onu göndereceğim pythonda

# kendi çözümüm son testte bazı yerlerde takıldı aslında sorun yok gibi ama tekrarlı sayılardan mı neyden bilemedim bir sebep ile çöküyor.gpt sonucunu gönderdim o sebep ile

# direkt ile seferde yaptığım çözüm
# Accepted Runtime: 33 ms
# class Solution:
#     def minOperations(self, grid: list[list[int]], x: int) -> int:
#         total = 0
#         newGrid:list[int] = [col for row in grid for col in row]
#         for i in newGrid:
#             total += i
#         average = total / len(newGrid)
#         distanceList = []
#         for i in newGrid:
#             distanceList.append(abs(i - average))
#         minValue = min(distanceList)

#         baseValue = int(average + minValue) if int(average+minValue) in newGrid else int(average - minValue)

#         result = 0
#         for i in newGrid:
#             tempValue = abs(baseValue - i) / x
#             if tempValue - int(tempValue) != 0:
#                 return -1
#             else:
#                 result += tempValue 
#         return int(result)


# üstteki kodu gpt ile performanslı hale getirmesini istedim.
#Accepted Runtime: 30 ms
# class Solution:
#     def minOperations(self, grid: list[list[int]], x: int) -> int:
#         newGrid = [col for row in grid for col in row]
#         newGrid.sort()
#         median = newGrid[len(newGrid) // 2]
#         result = 0
#         for num in newGrid:
#             tempValue = abs(median - num) / x
#             if tempValue != int(tempValue):
#                 return -1
#             result += int(tempValue)
#         return result


# gpt ye kendin en hızlı çözümü üret dedim çıktı bu 
#Accepted Runtime: 35 ms
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        flat_grid = [num for row in grid for num in row]
        flat_grid.sort()
        median = flat_grid[len(flat_grid) // 2]
        operations = 0
        for num in flat_grid:
            diff = abs(num - median)
            if diff % x != 0:
                return -1
            operations += diff // x
        return operations

def tester(number:int, grid: list[list[int]], x: int, result:int):
    res = Solution().minOperations(grid, x)
    print(f"Test {number} Başarılı" if res == result else f"Test {number} Başarısız " + "result =  " + str(res) + "    expected = " + str(result))

if __name__ == "__main__":
    testArray = []
    testArray.append([[[2,4],[6,8]], 2, 4])
    testArray.append([[[1,5],[2,3]], 1, 5])
    testArray.append([[[1,2],[3,4]], 2, -1])
    testArray.append([[[2,4],[6,8]], 2, 4])
    testArray.append([[[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]], 84, 45])
        
    
    for i,test in enumerate(testArray):
        tester(i+1,test[0],test[1],test[2])






