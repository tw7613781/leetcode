const assert = require('assert')

const firstUniqChar = function (s) {
  for (let i = 0; i < s.length; i++) {
    const ch = s.charAt(i)
    if (s.indexOf(ch) === i && s.indexOf(ch, i + 1) === -1) {
      return i
    }
  }
  return -1
}

let s, ret

s = 'leetcode'
ret = firstUniqChar(s)
assert.equal(ret, 0)

s = 'loveleetcode'
ret = firstUniqChar(s)
assert.equal(ret, 2)

s = ''
ret = firstUniqChar(s)
assert.equal(ret, -1)

s = 'abcdefj'
ret = firstUniqChar(s)
assert.equal(ret, 0)

s = 'aabbccddee'
ret = firstUniqChar(s)
assert.equal(ret, -1)

s = 'aabbccdde'
ret = firstUniqChar(s)
assert.equal(ret, 8)
