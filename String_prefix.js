const assert = require('assert')

const func = (s) => {
  if (s.length === 0) return ''
  let ret = ''
  const minLength = Math.min(...s.map(str => str.length))
  for (let i = 0; i < minLength; i++) {
    const target = s[0][i]
    for (let j = 1; j < s.length; j++) {
      if (s[j][i] !== target) {
        return ret
      }
    }
    ret += target
  }
  return ret
}

let s, exp, ret

s = ['flower', 'flow', 'flight']
exp = 'fl'
ret = func(s)
assert.equal(ret, exp)

s = ['dog', 'racecar', 'car']
exp = ''
ret = func(s)
assert.equal(ret, exp)

s = []
exp = ''
ret = func(s)
assert.equal(ret, exp)

s = ['dog']
exp = 'dog'
ret = func(s)
assert.equal(ret, exp)
