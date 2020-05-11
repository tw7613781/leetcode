https://leetcode.com/submissions/detail/145340848/
二分查找，主要练习ts的写法
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    var start = 0;
    var end = nums.length - 1;
    var mid = (start + end) / 2 | 0;
    if (target <= nums[0])
        return 0;
    if (target > nums[end])
        return end + 1;
    if (target == nums[end])
        return end;
    while (mid != start) {
        var val = nums[mid];
        if (target == val) {
            return mid;
        }
        else if (target > val) {
            start = mid;
        }
        else {
            end = mid;
        }
        mid = (start + end) / 2 | 0;
    }
    return mid + 1;
};
var nums = [3, 7, 11, 19, 22, 27, 45];
console.log(searchInsert(nums, 0));
