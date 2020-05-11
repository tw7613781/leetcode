const assert = require('assert')

function decodeString(s) {
    const stack = []
    for (const ele of s) {
        if (ele !== "]") {
            stack.push(ele)
        } else {
            let str = []
            let num = []
            let top
            do {
                top = stack.pop()
                str.push(top)
            } while(top !== "[")
            str = str.reverse().slice(1).join("")
            do {
                top = stack.pop()
                num.push(top)
            }
            while (top !== undefined && (top >= "0" && top <= "9") ) 
            num = Number(num.reverse().slice(1).join(""))
            if (top !== undefined) stack.push(top)
        
            let repeatStr = ""
            if (num === 0 || num === 1) { 
                repeatStr = str 
            } else {
                while(num > 0) {
                    repeatStr = repeatStr + str
                    num --
                }
            }
            for ( const s of repeatStr) {
                stack.push(s)
            }
        }
    }
    return stack.join("")
}

s = "3[a]2[bc]"
ret = decodeString(s)
assert.equal(ret, "aaabcbc")

s = "2[abc]3[cd]ef"
ret = decodeString(s)
assert.equal(ret, "abcabccdcdcdef")

s = "3[a2[c]]"
ret = decodeString(s)
assert.equal(ret, "accaccacc")

s = "2[a2[b]c]"
ret = decodeString(s)
assert.equal(ret, "abbcabbc")

