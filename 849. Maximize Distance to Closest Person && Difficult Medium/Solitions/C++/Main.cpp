// 849. Maximize Distance to Closest Person && Difficult Medium

#include <iostream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int prev = -1, result = 0;
        for (int i = 0; i < seats.size(); i++) {
            if (seats[i] == 1) {
                if (prev == -1) {
                    result = max(result, i);
                } else {
                    result = max(result, (i - prev) / 2);
                }
                prev = i;
            }
        }
        if (seats[seats.size() - 1] == 0) {
            result = max(result, (int)seats.size() - 1 - prev);
        }
        return result;
    }
};

int main()
{
     vector<pair<vector<int>, int>> testArray = {
        {{1, 0, 0, 0, 1, 0, 1}, 2},
        {{1, 0, 0, 0}, 3},
        {{0, 1}, 1},
        {{1, 1, 0, 1, 1}, 1},
        {{1, 0, 0, 1}, 1}
    };

    Solution sol;
    auto start = chrono::high_resolution_clock::now();
    
    for (int i = 0; i < testArray.size(); i++) {
        int res = sol.maxDistToClosest(testArray[i].first);
        cout << "Test " << i + 1 << (res == testArray[i].second ? " Başarılı " : " Başarısız ")
             << "Res = " << res << " Except = " << testArray[i].second << endl;
    }

    auto processTime = chrono::high_resolution_clock::now() - start;
    auto ns = chrono::duration_cast<chrono::nanoseconds>(processTime).count();

    cout << ns << endl;

    string msTime = "000000" + to_string(ns);
    msTime = msTime.substr(0, msTime.size() - 6) + "." + msTime.substr(msTime.size() - 6);

    cout << msTime << endl;
    cout << "Süre(ms) = " << stof(msTime) << endl;

    return 0;
}

