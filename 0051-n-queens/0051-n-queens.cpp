class Solution {
public:
    void addQ(vector<pair<int,int>>& queens, vector<vector<string>> &comb, int n)
    {
        vector<string> a;
        string x = "";
        for (int i = 0; i < n; i++)
            x += '.';
        
        for (auto i : queens)
        {
            string temp = x;
            temp[i.second] = 'Q';
            // push back will create copy which is why
            // our string temp can be redeclared on the
            // next iteration without affecting the 
            // one that is already pushed into the vector
            a.push_back(temp);
        }
        
        comb.push_back(a);
        }
    void Queens(int row, vector<pair<int, int>> &queens, int n, vector<vector<string>> &comb)
    {
    // for (auto x : queens)
    //     cout << x.first << ' ' << x.second << ' ';
    // cout << endl;
    if (row == n)
    {
        addQ(queens, comb, n);
        return;
    }
    for (int i = 0; i < n; i++)
    {
        int goNext = false;
        for (auto x : queens)
            if (row - x.first == abs(x.second - i) || x.second == i)
            {
                goNext = true;
                break;
            }
        if (!goNext)
        {
            queens.push_back(make_pair(row, i));
            Queens(row + 1, queens, n, comb);
            queens.pop_back();
        }
        // cout << i << endl;
    }
}
    vector<vector<string>> solveNQueens(int n) {
        vector<pair<int,int>> queens;
        vector<vector<string>> comb;
        Queens(0, queens, n, comb);
        return comb;
    }
};