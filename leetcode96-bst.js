// key: Let t(n) be the total number of BSTs with n nodes. The total number of BSTs with i at the root is t(i – 1) t(n – i). The two terms are multiplied together because the arrangements in the left and right subtrees are independent. 

const assert = require('assert')

function numTrees(n) {
    treeNum = new Array(n+1).fill(0)
    treeNum[0] = 1
    treeNum[1] = 1
    const calN = (n) => {
        if (treeNum[n] !== 0) { return treeNum[n]}
        else {
            for(let i = 1; i<=n; i++) {
                treeNum[n] += calN(i-1) * calN(n-i)
            }
            return treeNum[n]
        }
    }
    for(let i = 1; i <=n; i++){
        calN(i)
    }
    return treeNum[n]
}


n = 1
ret = numTrees(n)
assert.equal(ret, 1)

n = 2
ret = numTrees(n)
assert.equal(ret, 2)

n = 3
ret = numTrees(n)
assert.equal(ret, 5)

n = 4
ret = numTrees(n)
assert.equal(ret, 14)