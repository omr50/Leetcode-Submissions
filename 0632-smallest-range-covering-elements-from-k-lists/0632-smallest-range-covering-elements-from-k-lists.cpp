class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
    int maximum = -1000000, minimum = 1000000;
    vector<int> arr[200001];
    for (int i = 0; i < nums.size(); i++)
    {
        for (auto x : nums[i])
        {
            maximum = max(maximum, x);
            minimum = min(minimum, x);
            arr[x+100000].push_back(i); 
        }
    }
    unordered_map<int, int> uniques;
    vector<int> range;

    int l = minimum + 100000, r = minimum + 100000, curr = 0;
    range.push_back(minimum + 100000);
    range.push_back(maximum + 100000);
        if (minimum == maximum)
        {
            range[0] -= 100000;            
            range[1] -= 100000;

            return range;
        }

    int lcurr = 0, rcurr = 0;        
    while (r <= maximum+100000)
    {


        if (!arr[r].empty())
        {

            if (uniques.find(arr[r][rcurr]) == uniques.end())
                uniques[arr[r][rcurr]] = 1;
            else
                uniques[arr[r][rcurr]]++;

            while (uniques.size() == nums.size())
            {
                if (!arr[l].empty())
                {
                if (uniques[arr[l][lcurr]])
                    uniques[arr[l][lcurr]]--;
                if (uniques[arr[l][lcurr]] == 0)
                    uniques.erase(arr[l][lcurr]);
                if (range[1] - range[0] > r - l)
                {

                    range[0] = l;
                    range[1] = r;
                }
                if (lcurr + 1== arr[l].size())
                {
                    lcurr = 0;
                    l++;
                }
                else
                    lcurr++;
            }
                else
                    l++;
            }
            if (rcurr + 1== arr[r].size())
            {
                rcurr = 0;
                r++;

            }
            else
                rcurr++;
        }
        else
            r++;

    
    }


    range[0] -= 100000;
    range[1] -= 100000;
    return range;
    }
};