const assert = require('assert')

// s is string
const countAndSay = (s) => {
  let count = 1
  let ret = ''
  for (let i = 1; i < s.length; i++) {
    if (s[i] !== s[i - 1]) {
      ret += count.toString()
      ret += s[i - 1].toString()
      count = 1
    } else count++
  }
  ret += count
  ret += s[s.length - 1]

  return ret
}

// s is number`
const main = (n) => {
  let ret = '1'
  let start = '1'
  for (let i = 0; i < n - 1; i++) {
    ret = countAndSay(start)
    start = ret
  }
  return ret
}

let s, expect, ret

s = 1
expect = '1'
ret = main(s)
assert.equal(ret, expect)

s = 4
expect = '1211'
ret = main(s)
assert.equal(ret, expect)

s = 10
expect = '13211311123113112211'
ret = main(s)
assert.equal(ret, expect)
