// https://leetcode.com/problems/first-bad-version/description/
// 使用binary search的时候，如果是返回两个状态，通过二分查找，算法会逼近一个状态的边界

/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let low = 1;
        let high = n;
        let mid = (low+high)/2 | 0;
        while(low <= high ){
            if(isBadVersion(mid)){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
            mid = (low+high)/2 | 0;
        }
        if(high<1) return 1;
        else return high+1;
    };
};