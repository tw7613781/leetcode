// https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
// 此体本来是用hash就很容易做了，但是它不允许使用额外的空间，所以没法用最直接简单的那种hash，但是它自己本身的数据特点让它自己本身可以跟本身做hash，这样就解决问题了，但是参看别人的代码，好像使用额外空间set，也能通过，就不知道它搞什么鬼了。例子中很好的介绍的set怎么用和遍历array时候的foreach函数的方法

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let len = nums.length;
    let star = len + 1;
    let res = [];
    let i =1;
    while(i<=len){
        index = i-1;
        if(nums[index]==i || nums[index] == star){
            i++;
        }
        else if(nums[index] == nums[nums[index]-1]){
            res.push(nums[index]);
            nums[index] = star;
            i++;
        }
        else{
            let tmp = nums[index];
            nums[index] = nums[nums[index]-1];
            nums[tmp-1] = tmp;
        }
    }
    return res;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates1= function(nums) {
    let duplicates = [];
    let set = new Set();
    nums.forEach(n => {
      if (set.has(n)) {
        duplicates.push(n);
        return;
      }
      set.add(n);
    });
    return duplicates;
  };


let nums = [4,3,2,7,8,2,3,1];
console.log(findDuplicates(nums));