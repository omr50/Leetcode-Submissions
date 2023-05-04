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
    vector<int> rightSideView(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> output;
        if (!root)
            return output;
        q.push(root);
        while (!q.empty()) {
            // get the right most value then
            // get the next layer.
            output.push_back(q.back()->val);
            int len = q.size();
            for (int i = 0; i < len; i++) {
                if (q.front()->left) 
                    q.push(q.front()->left);
                
                if (q.front()->right) 
                    q.push(q.front()->right);
                
                q.pop();
                
            }
            
        }

        return output;

    }
};