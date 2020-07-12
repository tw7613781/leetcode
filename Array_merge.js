const assert = require('assert')

const func = (num1, m, num2, n) => {
  let indexN = 0
  let indexM = 0
  let lastM = m - 1
  while (indexM < m + n) {
    if (indexM === m + indexN) {
      for (let i = indexN; i < n; i++) {
        num1[indexM] = num2[indexN]
        indexM++
        indexN++
      }
      return num1
    }
    if (num2[indexN] < num1[indexM]) {
      lastM++
      for (let i = lastM; i > indexM; i--) {
        num1[i] = num1[i - 1]
      }
      num1[indexM] = num2[indexN]
      indexN++
      if (indexN === n) {
        return num1
      }
    }
    indexM++
  }
  return num1
}

let nums1, m, nums2, n, exp, ret

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
exp = [1, 2, 2, 3, 5, 6]
ret = func(nums1, m, nums2, n)
console.log(ret, exp)

nums1 = [0, 0, 0]
m = 0
nums2 = [2, 5, 6]
n = 3
exp = [2, 5, 6]
ret = func(nums1, m, nums2, n)
console.log(ret, exp)

nums1 = [2, 5, 6]
m = 3
nums2 = []
n = 0
exp = [2, 5, 6]
ret = func(nums1, m, nums2, n)
console.log(ret, exp)

nums1 = []
m = 0
nums2 = []
n = 0
exp = []
ret = func(nums1, m, nums2, n)
console.log(ret, exp)

nums1 = [1, 2, 0, 0, 0]
m = 2
nums2 = [2, 5, 6]
n = 3
exp = [1, 2, 2, 5, 6]
ret = func(nums1, m, nums2, n)
console.log(ret, exp)

nums1 = [1, 2, 100, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
exp = [1, 2, 2, 5, 6, 100]
ret = func(nums1, m, nums2, n)
console.log(ret, exp)
