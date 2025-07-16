using System.Diagnostics.Metrics;
using System.Text.Json;
using System.Text.Json.Serialization;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine(MaximumLength([1,2,3,4]));
        Console.WriteLine(MaximumLength([1,2,1,1,2,1,2]));
        Console.WriteLine(MaximumLength([1,3]));
        Console.WriteLine(MaximumLength([1, 5, 9, 4, 2]));
    }
    public static int MaximumLength(int[] nums)
    {
        if (nums.Length <= 2) return nums.Length;

        int countEven = 0, countOdd = 0;
        int even_len = 0, odd_len = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] % 2 == 0)
            {
                countEven++;
                even_len = Math.Max(even_len, odd_len + 1);
            }
            else
            {
                countOdd++;
                odd_len = Math.Max(odd_len, even_len + 1);
            }
        }

        int sameParityMax = Math.Max(countEven, countOdd);
        int altMax = Math.Max(even_len, odd_len);

        // Alternating alt dizi en az 2 elemanlı olmalı
        if (altMax < 2) altMax = 0;

        return Math.Max(sameParityMax, altMax);
    }

}