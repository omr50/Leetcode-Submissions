/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> output;
        vector<int> currLayer;
        
        queue<TreeNode*> q;
        if (!root)
            return output;
        q.push(root);
        int counter = 1;
        while (!q.empty()){
            
            int len = q.size();
            
            for (int i = 0; i < len; i++) {
                currLayer.push_back(q.front()->val);
                
                if (q.front()->left)
                    q.push(q.front()->left);
                
                if (q.front()->right)
                    q.push(q.front()->right);
                
                q.pop();
            }
            if (!(counter % 2))
                reverse(currLayer.begin(), currLayer.end());
            output.push_back(currLayer);
            
            currLayer.clear();
            
            counter++;
            
        }
        
        return output;
    }
};