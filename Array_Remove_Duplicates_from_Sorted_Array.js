/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let len = nums.length;
    for(let i = len-1; i>0; i--){
        if(nums[i] == nums[i-1]){
            nums.splice(i,1);
        }
    }  
    return nums.length;
};

nums = [1,1,2];
nums = [];
nums = [1,2,3,4]
console.log(removeDuplicates(nums));