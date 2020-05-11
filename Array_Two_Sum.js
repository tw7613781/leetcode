/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  var len = nums.length;
  var res = [];
  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      if (nums[i] + nums[j] == target) {
        res.push(i)
        res.push(j)
        return res
      }
    }
  }

};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const memo = new Map();

  for (let i = 0; i < nums.length; i++) {
    let value = nums[i];
    let complement = target - value;

    if (memo.has(complement)) {
      let complementIdx = memo.get(complement).find((element) => element !== i);

      console.log("======", complementIdx, "==========", i);
      if (complementIdx !== undefined) { return [complementIdx, i]; }
    }

    if (!memo.has(value)) {
      memo.set(value, []);
    }

    memo.get(value).push(i);
  }
  return [];
};


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let result = []
  let set = new Set()
  for (let i = 0; i <= nums.length; i++) {
    if (!set.has(nums[i])) {
      set.add(target - nums[i]);
    }
    else {
      result.push(nums.indexOf(target - nums[i]))
      result.push(i);

    }

  }
  return result
};