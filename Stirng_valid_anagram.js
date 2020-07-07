const assert = require('assert')

// const func = (s, t) => {
//   if (s.length !== t.length) {
//     return false
//   }
//   for (const ch of s) {
//     const pos = t.indexOf(ch)
//     if (pos === -1) {
//       return false
//     } else {
//       t = t.replace(t[pos], '')
//     }
//   }
//   if (t === '') {
//     return true
//   } else {
//     return false
//   }
// }

const func = (s, t) => {
  if (s.length !== t.length) return false
  const dict = Array(26).fill(0)
  const anthor = 'a'.charCodeAt(0)
  for (let i = 0; i < s.length; i++) {
    dict[s[i].charCodeAt(0) - anthor]++
    dict[t[i].charCodeAt(0) - anthor]--
  }
  for (let i = 0; i < dict.length; i++) {
    if (dict[i] !== 0) {
      return false
    }
  }
  return true
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

s = ''
t = ''
ret = func(s, t)
assert.equal(ret, true)

s = 'abcdef'
t = 'fedcbac'
ret = func(s, t)
assert.equal(ret, false)
