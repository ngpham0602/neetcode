class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        
        map<int, int> count;
        for (int x : nums) {
            count[x]++;
        } 
        
        vector<pair<int, int>> v(count.begin(), count.end());

        sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
        });

        vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(v[i].first);
        }
        return result;

        
    }
};
