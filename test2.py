# int index = 0;
# int result = 0;
#
# for(int i = 1; i < n; i++){
#     int total = A[i] + i + A[index] - index;
#     result = max(result, total);
#     if(A[i] - i > A[index] - index){
#         index = i;
#     }
# }
# return result;




A = [1, 3, -3]

A = [-8,4,0,5,-3,6]

def solution(A):

    i=0
    size=len(A)
    result1 = 0
    while i < size:
        total = A[i] + i
        result1 = max(result1,total)
        i+=1
    i = 0
    result2 = 0
    while i<size:
        total = A[i] - i
        result2 = max(result2,total)
        i+=1
    return result1+result2


print solution(A)