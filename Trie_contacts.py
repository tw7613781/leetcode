# 4
# add hack
# add hackerrank
# find hac
# find hak

class TrieNode:

    __slot__ = ['children','isEndofWord','NumberofWord']

    def __init__(self):
        self.children = [None]*26
        self.isEndofWord = False
        self.NumberofWord = 0

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode();


    def _charToIndex(self,ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        point = self.root
        for ch in word:
            index = self._charToIndex(ch)
            if point.children[index] is None:
                point.children[index] = self.getNode()
            point = point.children[index]
            point.NumberofWord += 1
        point.isEndofWord = True


    def find(self,word):
        point = self.root
        flag = True
        for ch in word:
            index = self._charToIndex(ch)
            if point.children[index] is not None:
                point = point.children[index]
            else:
                flag = False
                break
        if flag == False:
            return 0
        else:
            return point.NumberofWord


n = int(raw_input().strip())
root = Trie()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        root.insert(contact)
    else:
        print root.find(contact)

#
# Using Dict to reduce memory usage.

# root = {'childrens': 0}
#
# def add_word(word):
#     node = root
#     node['childrens'] += 1
#
#     for l in word:
#         n = node.get(l, None)
#         if n is None:
#             n = {'childrens': 0}
#             node[l] = n
#         node = n
#         node['childrens']  += 1
#
# def search_partial(prefix):
#     node = root
#     for l in prefix:
#         if l not in node:
#             return 0
#         node = node[l]
#     return node['childrens']
#
# n = int(raw_input().strip())
# for a0 in xrange(n):
#     op, contact = raw_input().strip().split(' ')
#     if op == 'add':
#         add_word(contact)
#     else:
#        print search_partial(contact)