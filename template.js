const assert = require('assert')

const func = (s, t) => {
}

let s, t, ret

s = 'anagram'
t = 'nagaram'
ret = func(s, t)
assert.equal(ret, true)

s = 'rat'
t = 'car'
ret = func(s, t)
assert.equal(ret, false)
