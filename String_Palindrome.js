const assert = require('assert')

const validAlpha = (ch) => {
  if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z')) return true
  return false
}

const validNum = (ch) => {
  if (ch >= '0' && ch <= '9') return true
  return false
}

const validAlphanum = (ch) => {
  return validAlpha(ch) || validNum(ch)
}

const cleanString = (s) => {
  let ret = ''
  for (const ch of s) {
    if (validAlphanum(ch)) {
      ret += ch.toLowerCase()
    }
  }
  return ret
}

const func = (s) => {
  s = cleanString(s)
  let start = 0
  let end = s.length - 1
  while (start < end) {
    if (s[start] !== s[end]) {
      return false
    }
    start++
    end--
  }
  return true
}

let s, ret

s = 'A man, a plan, a canal: Panama'
ret = func(s)
assert.equal(ret, true)

s = 'race a car'
ret = func(s)
assert.equal(ret, false)

s = ''
ret = func(s)
assert.equal(ret, true)

s = 'ab_a'
ret = func(s)
assert.equal(ret, true)
