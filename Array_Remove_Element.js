// https://leetcode.com/problems/remove-element/description/
// difficulty level: easy
// just found the element, and use splice function to remove it, the better way is to traverse from end to 0
// time complexity is depends, it vary between O(n) to O(n^2)

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let i =0;
    let len = nums.length;
    while(i<len){
        if(nums[i] == val){
            nums.splice(i,1);
            len--;
        }
        else i++;
    }
    return nums.length;
};


let nums = [3,2,2,3];
let val = 2;
console.log(removeElement(nums,val));