int rob(vector<int>& nums) {
    int n = nums.size();
    if(n==0) return 0;
    if(n==1) return nums[0];
    vector<int> dp1={0,nums[0]},	dp2={nums[n-1],nums[n-1]};
    for(int i=2;i< n;++i){
            dp1.push_back(max(dp1[i-1], nums[i-1]+dp1[i-2])); //rob 0
            dp2.push_back(max(dp2[i-1], nums[i-1]+dp2[i-2])); //rob n-1

    }
    return max( dp1[n-1], dp2[n-2]); //dp[n-2] due to not rob n-2

}
