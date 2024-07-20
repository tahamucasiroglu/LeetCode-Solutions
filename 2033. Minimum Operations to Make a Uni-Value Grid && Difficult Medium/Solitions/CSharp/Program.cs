internal class Program
{
    private static void Main(string[] args)
    {
        var testData = new (int[][] grid, int x, int expected)[]
        {
            (new int[][] { new int[] { 2, 4 }, new int[] { 6, 8 } }, 2, 4),
            (new int[][] { new int[] { 1, 5 }, new int[] { 2, 3 } }, 1, 5),
            (new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } }, 2, -1),
            (new int[][] {
                new int[] { 980, 476, 644, 56 },
                new int[] { 644, 140, 812, 308 },
                new int[] { 812, 812, 896, 560 },
                new int[] { 728, 476, 56, 812 }
            }, 2, 41)
        };
    

     for (int i = 0; i < testData.Length; i++)
        {
            int[][] grid = testData[i].grid;
            int x = testData[i].x;
            int expected = testData[i].expected;
            int result = MinOperations(grid, x);
            if(expected == result)
            {
                Console.WriteLine($"Test case {i + 1} Success : Expected {expected}, Result {result}");
            }
            else
            {
                Console.WriteLine($"Test case {i + 1} Failed : Expected {expected}, Result {result}");
            }
            
        }
    }
    // ilk çözüm ama son elemanda elendi çok karışık oldu zaten çalışsada sıkıntı. teste soktum çalışanlarda da 76ms bu nedir. Başarısız bu
    // private static int MinOperations(int[][] grid, int x) 
    // {
    //     int cols = grid.Length;
    //     int rows = grid[0].Length;

    //     int[] newGrid = new int[rows * cols];
    //     int total = 0;
    //     for(int i = 0; i < cols*rows; i++)
    //     {
    //         newGrid[i] = grid[i/cols][i%rows];
    //         total += newGrid[i];
    //     }
    //     double average = total / newGrid.Length;
    //     int[] baseValue = new int[5]{0,0,0,0,0};
    //     for(int i = 0; i < newGrid.Length; i++)
    //     {
    //         if(newGrid[i] >= average)
    //         {
    //             baseValue[0] = newGrid[i - 2 >= 0 ? i - 2 : 0];
    //             baseValue[1] = newGrid[i - 1 >= 0 ? i - 1 : 0];
    //             baseValue[2] = newGrid[i];
    //             baseValue[3] = newGrid[i + 1 < newGrid.Length ? i + 1 : newGrid.Length - 1];
    //             baseValue[4] = newGrid[i + 2 < newGrid.Length ? i + 2 : newGrid.Length - 2];
    //         }
    //     }
    //     int[] result = new int[5]{0,0,0,0,0};
    //     for(int i = 0; i < newGrid.Length; i++)
    //     {
    //         for(int j = 0; j < 5; j++)
    //         {
    //              if(result[j] != -1 && Math.Abs(newGrid[i] - baseValue[j]) % x == 0)
    //             {
    //                 result[j] += Math.Abs(newGrid[i] - baseValue[j]) / x;
    //             }
    //             else
    //             {
    //                 result[j] = -1;
    //             }
    //         }
    //     }
    //     int res = 1000;
    //     for(int i = 0; i < 5; i++){
    //         if(result[i]>=0 && result[i] < res)
    //         {
    //             res = result[i];
    //         }
    //     }
    //     return res == 1000 ? -1 : res;
    // }




    // gpt çözümü ile fark ettim ben hep ortalama alıyrum gpt ise median almakta ortalama daha yakın vermeli bence ama median sonuçları işlemi hızlandırdığı için bieinceiler arasında
        
    private static int MinOperations(int[][] grid, int x) 
    {
        List<int> flatGrid = new List<int>();
        foreach (var row in grid)
        {
            flatGrid.AddRange(row);
        }
        flatGrid.Sort();
        int median = flatGrid[flatGrid.Count / 2];
        int operations = 0;
        foreach (var num in flatGrid)
        {
            int diff = Math.Abs(num - median);
            if (diff % x != 0)
            {
                return -1;
            }
            operations += diff / x;
        }
        return operations;
    }
















}



    // testArray = []
    // testArray.append([[[2,4],[6,8]], 2, 4])
    // testArray.append([[[1,5],[2,3]], 1, 5])
    // testArray.append([[[1,2],[3,4]], 2, -1])
    // testArray.append([[[2,4],[6,8]], 2, 4])
    // testArray.append([[[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]], 84, 45])