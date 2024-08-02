# 849. Maximize Distance to Closest Person && Difficult Medium
import time 



# ilk çözüm tam başarı sıralama kötü  107ms
# class Solution:
#     def maxDistToClosest(self, seats: list[int]) -> int:
#         length = len(seats)
#         maxSeats = 0
#         tempSeats = 0
#         i = 0
#         while i<length:
#             if seats[i] == 0:
#                 tempSeats += 1
#             else:
#                 maxSeats = max(maxSeats, tempSeats/2+0.5)
#                 tempSeats = 0
#             i+=1
#         if seats[0] == 0:
#             maxSeats = max(maxSeats, seats.index(1))
#         if seats[-1] == 0:
#             seats.reverse()
#             maxSeats = max(maxSeats, seats.index(1))
#         return int(maxSeats)





# biraz farklı 102 ms
# class Solution: 
#     def maxDistToClosest(self, seats: list[int]) -> int:
#         length = len(seats)
#         maxSeats = 0
#         i = 0
#         while i<length:
#             if seats[i] == 1:
#                 j = i + 1 
#                 while j < length:
#                     if seats[j] == 1:
#                         maxSeats = max(maxSeats, (j-i)//2)
#                         i = j - 1
#                         break
#                     j+=1
#             i+=1

#         if seats[0] == 0:
#             maxSeats = max(maxSeats, seats.index(1))
#         if seats[-1] == 0:
#             i = 1
#             while True:
#                 if seats[-i] == 1:
#                     maxSeats = max(maxSeats, i-1)
#                     break
#                 i+=1
#         return maxSeats




# birincinin kodunu koydum 107ms verdi bu kod 102 ms verdi. bu ms olayı baya saçma
class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        prev = 0
        result = 0
        for i,n in enumerate(seats):
            if n:
                result = max(result, (i-prev)//2)
                prev = i
        if not seats[0]:
            result = max(result, seats.index(1))
        if not seats[-1]:
            result = max(result, len(seats) - 1 - prev)
        return result







if __name__ == "__main__":
    testArray = [
        [[1,0,0,0,1,0,1], 2],
        [[1,0,0,0], 3],
        [[0,1], 1],
        [[1,1,0,1,1], 1],
        [[1,0,0,1], 1]
    ]

    print(testArray[1][0][-4])

    sol = Solution()
    start = time.perf_counter_ns()
    for i,n in enumerate(testArray):
        res = sol.maxDistToClosest(n[0])
        print(f"Test {i+1} {("Başarılı" if res == n[1] else "Başarısız")} Res = {res}  Except = {n[1]}")

    processTime = time.perf_counter_ns() - start
    print(processTime)
    msTime = "000000"+str(processTime)
    print(msTime)
    msTime = msTime[:-6] + "." + msTime[-6:]
    print(msTime)
    print("Süre(ms) = " + f"{float(msTime)}")