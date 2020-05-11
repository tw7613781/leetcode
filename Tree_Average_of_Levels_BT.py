# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# width first search to get all element value and level, then use 2 list to calculate average value of each level

from Tree_Binary_Search_Tree_Library import Node

node = Node(8)
node.insert(5)
node.insert(12)
node.insert(2)
node.insert(6)
node.insert(13)


def averageOfLevels(root):
    res = []
    queue = []
    level = 0
    queue.insert(0, [root, level])
    while queue:
        run = queue.pop()
        level = run[1]
        res.append([run[0].val, level])
        if run[0].left:
            queue.insert(0, [run[0].left, level + 1])
        if run[0].right:
            queue.insert(0, [run[0].right, level + 1])
    sum = [0] * 10000
    ct = [0] * 10000
    for element in res:
        sum[element[1]] += element[0]
        ct[element[1]] += 1
    i = 0
    ans = []
    while ct[i] != 0:
        ans.append(sum[i] / ct[i])
        i += 1

    return ans




res = averageOfLevels(node)
print(res)

