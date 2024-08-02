internal class Program
{
    private static void Main(string[] args)
    {
        Solution solution= new Solution();
        Console.WriteLine(solution.MaxDistToClosest(new int[] { 1, 0, 0, 0, 1, 0, 1 }) == 2); 
        Console.WriteLine(solution.MaxDistToClosest(new int[] { 1, 0, 0, 0}) == 3); 
        Console.WriteLine(solution.MaxDistToClosest(new int[] { 0, 1}) == 1); 
        Console.WriteLine(solution.MaxDistToClosest(new int[] { 1, 1, 0, 1, 1}) == 1); 
        Console.WriteLine(solution.MaxDistToClosest(new int[] { 1, 0, 0, 1}) == 1);
        Console.WriteLine(solution.MaxDistToClosest(new int[] { 0, 0, 1}) == 2);
    }
}


// 85 ms
// public class Solution {
//     public int MaxDistToClosest(int[] seats) {
//         int prev = 0, result = 0;
//         for(int i = 0;i<seats.Length;i++)
//         {
//             if(seats[i] == 1)
//             {
//                 result = Math.Max(result, (i - prev) / 2);
//                 prev = i;
//             }
//         }
//         if(seats.First() == 0){
//             result = Math.Max(result, seats.First(p=>p==1));
//         }
//         if (seats.Last() == 0)
//         {
//             result = Math.Max(result, seats.Length - 1 - prev);
//         }
//         return result;
//     }
// }






// 80 ms 
public class Solution {
    public int MaxDistToClosest(int[] seats) {
        int prev = -1, result = 0;
        for (int i = 0; i < seats.Length; i++)
        {
            switch (seats[i])
            {
                case 1 when prev == -1:
                    result = Math.Max(result, i); prev = i; break;
                case 1 when prev != -1:
                    result = Math.Max(result, (i - prev) / 2); prev = i; break;
                case 0 when i == seats.Length - 1:
                    result = Math.Max(result, seats.Length - 1 - prev); break;
            }
        }
        return result;
    }
}