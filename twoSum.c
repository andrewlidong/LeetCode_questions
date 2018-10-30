class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> hash;
        vector<int> result;
        for (int i = 0; i < numbers.size(); i++) {
            int numberToFind = target - numbers[i];

//             if numberToFind is in map, return them
            if (hash.find(numberToFind) != hash.end()) {
//                 +` because indices are NOT zero based
                result.push_back(hash[numberToFind] + 1);
                return result;
            }

//             number not found.  Put it in the map.
            hash[numbers[i]] = i;
        }
        return result;
    }
};
