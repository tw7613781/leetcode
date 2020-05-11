// /**
//  * @param {number[]} numbers
//  * @param {number} target
//  * @return {number[]}
//  */
// var twoSum = function(numbers, target) {
//     const hash = new Map();
//     var res = [];
//     for(let i = 0; i<numbers.length; i++){
//         if(hash.has(target - numbers[i])){
//             index1 = hash.get(target - numbers[i]);
//             index2 = i;
//             res.push(index1+1);
//             res.push(index2+1);
//             return res;
//         }
//         else{
//             hash.set(numbers[i],i);
//         }
//     }
//     return res;
// };
var twoSum = function(numbers, target) {
    res = [];
    let i = 0;
    let j = numbers.length - 1;
    while(i<j){
        if( numbers[i] + numbers[j] > target){
            j--;
        }
        else if(numbers[i] + numbers[j] < target){
            i++;
        }
        else{
            res.push(i+1);
            res.push(j+1);
            return res;
        }
    }
    return res;
};


var numbers = [2, 7, 11, 15];
var target = 9;
console.log(twoSum(numbers, target));