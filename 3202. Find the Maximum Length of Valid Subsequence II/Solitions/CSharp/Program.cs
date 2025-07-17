using System.Diagnostics.Metrics;
using System.Text.Json;
using System.Text.Json.Serialization;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine(MaximumLength([1, 2, 3, 4], 2));
        Console.WriteLine(MaximumLength([1, 2, 1, 1, 2, 1, 2], 2));
        Console.WriteLine(MaximumLength([1, 3], 2));
        Console.WriteLine(MaximumLength([1, 5, 9, 4, 2], 2));
        Console.WriteLine(MaximumLength([1, 2, 3, 4, 5], 2));
        Console.WriteLine(MaximumLength([1, 4, 2, 3, 1, 4], 3));
        Console.WriteLine(MaximumLength([1, 7, 9], 10));
    }
    public static int MaximumLength(int[] nums, int k)
    {
        int[,] dp = new int[k, k];
        int ans = 0;

        foreach (var num in nums)
        {
            int x = num % k;
            int[] prevRow = new int[k];
            for (int y = 0; y < k; y++)
            {
                prevRow[y] = dp[y, x];
            }
            dp[x, x] = Math.Max(dp[x, x], 1);
            for (int y = 0; y < k; y++)
            {
                if (y == x) continue;
                dp[y, x] = Math.Max(dp[y, x], dp[x, y] + 1);
                ans = Math.Max(ans, dp[y, x]);
            }
            ans = Math.Max(ans, dp[x, x]);
        }

        return ans;
    }
}