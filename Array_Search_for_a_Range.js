// https://leetcode.com/problems/search-for-a-range/description/
// binary search的一个例子，寻找下边界和上边界，关键的区别在于当target == mid的时候该往上走还是往下走。

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let resL = -1;
    let resH = -1;
    let tag = 0;
    let low = 0;
    let high = nums.length-1;
    let mid = (low+high)/2 | 0;
    //find Low boundary
    while(low <= high){
        if (nums[mid] == target){
            tag = 1;
            high = mid - 1;
        }
        else if(nums[mid] < target){
            low = mid + 1;
        }
        else{
            high = mid -1;
        }
        mid = (low+high)/2 | 0;
    }
    if(tag == 1) resL = low;
    // cannot find the target
    else return [-1,-1];
    //find High boundary
    low = 0;
    high = nums.length-1;
    mid = (low+high)/2 | 0;   
    while(low <= high){
        if (nums[mid] == target){
            low = mid + 1;
        }
        else if(nums[mid] < target){
            low = mid + 1;
        }
        else{
            high = mid -1;
        }
        mid = (low+high)/2 | 0;
    }
    resH = high;
    return [resL, resH];
};

nums = [5,7,7,8,8,10];
target = 8;
nums = [1,2,2];
target = 2;
console.log(searchRange(nums, target));