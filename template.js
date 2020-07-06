const assert = require('assert')

var firstUniqChar = function (s) {

}

let s, ret

s = 'leetcode'
ret = firstUniqChar(s)
assert.equal(ret, 0)

s = 'loveleetcode'
ret = firstUniqChar(s)
assert.equal(ret, 2)
