const assert = require('assert')

const func = (str) => {
  str = str.trim().split(' ')[0].match(/^-\d+|^\d+|^\+\d+/)
  if (str === null) return 0
  else str = str[0]
  const num = Number(str)
  if (num < -(2 ** 31)) return -(2 ** 31)
  if (num > 2 ** 31 - 1) return 2 ** 31 - 1
  return num
}

let str, ret

str = '   -42'
ret = func(str)
assert.equal(ret, -42)

str = '4193 with words'
ret = func(str)
assert.equal(ret, 4193)

str = 'words and 987'
ret = func(str)
assert.equal(ret, 0)

str = '-91283472332'
ret = func(str)
assert.equal(ret, -2147483648)

str = '   3434dfaa 3434 32432 3434'
ret = func(str)
assert.equal(ret, 3434)

str = '   +3434dfaa 3434 32432 3434'
ret = func(str)
assert.equal(ret, 3434)

str = ''
ret = func(str)
assert.equal(ret, 0)

str = '.1'
ret = func(str)
assert.equal(ret, 0)
