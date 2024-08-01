internal class Program
{
    private static void Main(string[] args)
    {
        Solution solution= new Solution();
        Console.WriteLine(solution.Rob(new int[]{1,2,3,1})); // beklenen 4

    }
}

public class Solution {
    public int Rob(int[] nums) {
        int lenNums = nums.Length - 1;
        if (lenNums <= 2) {
            return nums.Max();
        }

        int res1_1 = nums[0];
        int res2_1 = nums[1];
        int res1_2 = Math.Max(res1_1, nums[1]);
        int res2_2 = Math.Max(res2_1, nums[2]);
        int res1_3 = 0;
        int res2_3 = 0;

        for (int i = 2; i < lenNums; i++) {
            res1_3 = Math.Max(res1_2, res1_1 + nums[i]);
            res1_1 = res1_2;
            res1_2 = res1_3;
            res2_3 = Math.Max(res2_2, res2_1 + nums[i + 1]);
            res2_1 = res2_2;
            res2_2 = res2_3;
        }

        return Math.Max(res1_3, res2_3);
    }
}