const assert = require('assert')

const func = (s, t) => {
  return s.indexOf(t)
}

let s, t, ret

s = 'hello'
t = 'll'
ret = func(s, t)
assert.equal(ret, 2)

s = 'aaaaa'
t = 'bba'
ret = func(s, t)
assert.equal(ret, -1)

s = 'aaaaa'
t = ''
ret = func(s, t)
assert.equal(ret, 0)
