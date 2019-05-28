# # 一个二叉树样例
#  class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)



# # def duplicateInArray(nums):
#     """
#     :type nums: List[int]
#     :rtype int
#     """
#     n = len(nums) # length of the nums
#     i = 0         # index
    
#     if n == 0:
#         return -1

#     for i in range(n):
#         if nums[i] >= n or nums[i] < 0:
#             return -1

#     while i < n:
#         if nums[i] == i:
#             i += 1
#         elif nums[i] == nums[nums[i]]:
#             return nums[i]
#         else:
#             temp = nums[i]
#             nums[i] = nums[temp]
#             nums[temp] = temp
    
#     return -1

# nums = [3, 1, -10, 1, 1, 4, 3, 10, 1, 1]
# a = duplicateInArray(nums)

#############################  14

# def duplicateInArray(nums):
#     """
#     :type nums: List[int]
#     :rtype int
#     """
    
#     n = len(nums)
#     label = [0] * n
    
#     for i in range(len(nums)):
#         if label[nums[i]] == 0:
#             label[nums[i]] = 1
#         else:
#             return nums[i]

# def duplicateInArray2(nums):
#     a = 1
#     b = len(nums) - 1
#     while a < b:
#         mid = (b+a)//2
#         count = 0
#         for i in range(len(nums)):
#             if a <= nums[i] <= mid:
#                 count += 1
#         if count > mid - a + 1:
#             b = mid
#         else:
#             a = mid +1
#     return b

    
#         # int l = 1, r = nums.size() - 1;
#         # while (l < r) {
#         #     int mid = l + r >> 1; // 划分的区间：[l, mid], [mid + 1, r]
#         #     int s = 0;
#         #     for (auto x : nums) s += x >= l && x <= mid;
#         #     if (s > mid - l + 1) r = mid;
#         #     else l = mid + 1;
#         # }
#         # return r;


# nums = [2, 3, 5, 4, 3, 2, 6, 7]
# a = duplicateInArray2(nums)
# print(a)

# ################### 16

# def replaceSpaces(s):
#     """
#     :type s: str
#     :rtype: str
#     """
    
#     n = len(s)
#     i = 0
    
#     while i < n:
#         if s[i] == ' ':
#             s = s[:i] + '%20' + s[i+1:]
#             n += 2
#             i += 2
#         i += 1
    
#     return s

# s = " h jPW5a   y rZ 4 6E"

# s = replaceSpaces(s)
# print(s)

############### 21

# def Fibonacci(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     nums = [0,1]
#     for i in range(n):
#         nums.append(nums[-1]+nums[-2])
        
#     return nums[-1]

# a = Fibonacci(39)
# print(a)

############## 22

# def findMin(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if nums == []: 
#         return -1
    
#     left = 0
#     right = len(nums) -1
#     mid = 0
#     while nums[left] >= nums[right]:

#         if right - left == 1:
#             mid = right
#             break

#         if nums[mid] == nums[left] == nums[right]:
#             return findMinInOrder(left,right)    
#         elif nums[mid] >= nums[left]:
#             left = mid
#         elif nums[mid] <= nums[right]: 
#             right = mid
#         mid = (left + right) // 2    
#     return nums[mid]

# def findMinInOrder(left,right):
#     res = nums[left]
#     for i in range(left,right+1):
#         if nums[i] < res:
#             res = nums[i]

#     return res
    
# nums = [1,0,1,1,1]
# a = findMin(nums)
# print(a)

################### 18

# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

# def buildTree(preorder, inorder):
#     """
#     :type preorder: List[int]
#     :type inorder: List[int]
#     :rtype: TreeNode
#     """
#     def rebuildTree(preorder,inorder,res):
#         while preorder:
#             root = preorder[0]
#             rootid = inorder.index(root)
#             res.append(root)
#             res += rebuildTree(preorder[1:1+rootid],inorder[:rootid],res)
#             res += rebuildTree(preorder[1+rootid:],inorder[rootid+1:],res)
#         return res
#     res = []
#     rebuildTree(preorder,inorder,res)

#     return res

# a = buildTree(preorder,inorder)
# print(a)

################################# 20

# class MyQueue(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack1 = []
#         self.stack2 = []        

#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         if self.stack1:
#             self.stack1.append(x)
#         else:
#             while self.stack2:
#                 self.stack1.append(self.stack2.pop())
#             self.stack1.append(x)

        

#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         if self.stack2:
#             return self.stack2.pop()
#         elif self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         else:
#             return None        

#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         if self.stack2:
#             item = self.stack2.pop()
#             self.stack2.append(item)
#             return item
#         elif self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             item = self.stack2.pop()
#             self.stack2.append(item)
#             return item
#         else:
#             return None           

#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         while self.stack1:
#             self.stack1.pop()
#         while self.stack2:
#             self.stack2.pop()

# a = MyQueue()
# a.push(4)

##########################23

# class Solution(object):
#     def hasPath(self, matrix, string):
#         """
#         :type matrix: List[List[str]]
#         :type string: str
#         :rtype: bool
#         """
#         def hasPathCore(self,x,y,string,matrix,label):
        
#             if not string:
#                 return True
            
#             if x<0 or x>=m or y<0 or y>=n or matrix[x][y]!= string[0] or label[x][y] == 1:
#                 return False
            
#             label[x][y] = 1 

#             if hasPathCore(self,x-1,y,string[1:],matrix,label) or \
#                 hasPathCore(self,x+1,y,string[1:],matrix,label) or \
#                 hasPathCore(self,x,y-1,string[1:],matrix,label) or \
#                 hasPathCore(self,x,y+1,string[1:],matrix,label):

#                 return True

#             label[x][y] = 0
#             return False    

#         if not matrix or not string:
#             return False
#         m = len(matrix)
#         n = len(matrix[0])
#         label = [[0]*n for i in range(m)]


#         for i in range(m):
#             for j in range(n):
#                 if hasPathCore(self,i,j,string,matrix,label):
#                     return True
#         return False
    
    

        
# matrix=[
#     ["C", "A", "A"], 
#     ["A", "A", "A"], 
#     ["B", "C", "D"]]

# s1="AAB" 
# a = Solution()
# print(a.hasPath(matrix,s1))

# s2="ASAE" 
# print(a.hasPath(matrix,s2))

#######################24

# k=0
# m=5
# n=6

# class Solution(object):
#     def movingCount(self, threshold, rows, cols):
#         """
#         :type threshold: int
#         :type rows: int
#         :type cols: int
#         :rtype: int
#         """
#         def movingCountCore(i,j,label,count):
#             if i < 0 or i >= rows or j < 0 or j >= cols or label[i][j] == 1:
#                 return count
            
#             if check(i,j,threshold):
#                 label[i][j] = 1
#                 count += 1
#             else:
#                 return count
            
#             count = movingCountCore(i-1,j,label,count)
#             count = movingCountCore(i+1,j,label,count)
#             count = movingCountCore(i,j-1,label,count)
#             count = movingCountCore(i,j+1,label,count)

#             return count

#         def check(i,j,threshold):
#             num = 0
#             while i > 0 or j > 0:
#                 num += i % 10
#                 num += j % 10

#                 i //= 10
#                 j //= 10

#             if num <= threshold:
#                 return True
#             else:
#                 return False


#         label = [[0]*cols for i in range(rows)]
#         count = 0

#         count = movingCountCore(0,0,label,count)

#         return count
        

# a = Solution()
# b = a.movingCount(k,m,n)
# print(b)
        

#################### 26

# n = 100
# n &= 0xFFFFFFFF
# num = 0
# while n != 0:
#     num += n & 1
#     n >>= 1
# print(num)

#################### 27

# class Solution(object):
#     def isNumber(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         dict = ['0','1','2','3','4','5','6','7','8','9']
#         i = 0
#         point = 0
#         flag = 0
#         if s[i] == '+' or s[i] =='-':
#             i += 1
#             flag = 1
        
#         while i < len(s):
            
#             if s[i] in dict:
#                 i += 1
#             elif s[i] == '.':
#                 point += 1
#                 if point != 1 or i == 0 or ((flag == 1)&(i == 1)):
#                     return False
#                 else:
#                     i += 1
#                     continue

#             elif s[i] == 'e' or s[i] == 'E':
#                 i += 1
#                 if i == len(s) or i == 1:
#                     return False
#                 else:
#                     break
#             else:
#                 return False
        
#         if i < len(s):
#             if (s[i] == '+' or s[i] =='-'):
#                 i += 1
        
#         while i < len(s):
#             if s[i] not in dict:
#                 return False
#             else:
#                 i += 1
    
            
#         return True

# s = "3.1416"
# a = Solution()
# print(a.isNumber(s))

################## 28
# class Solution(object):
#     def reOrderArray(self, array):
#         """
#         :type array: List[int]
#         :rtype: void
#         """
#         odd = []
#         even = []
        
#         for i in range(len(array)):
#             if array[i] % 2 == 1:
#                 odd.append(array[i])
#             else:
#                 even.append(array[i])
                
#         return odd + even

# array = [2, 9, 9, 5, 3, 2, 9, 6, 0, 4]

# a = Solution()
# print(a.reOrderArray(array))

#################### 39

# class Solution(object):
#     def hasSubtree(self, pRoot1, pRoot2):
#         """
#         :type pRoot1: TreeNode
#         :type pRoot2: TreeNode
#         :rtype: bool
#         """
#         if not pRoot1 or not pRoot2:
#             return False
#         else:
#             return self.checkTree(pRoot1, pRoot2)
            
#     def checkTree(self, pRoot1, pRoot2):
        
#         if pRoot2 == None:
#             return True
#         elif pRoot1 == None:
#             return False
#         res = False
#         if pRoot1.val == pRoot2.val:
#             res = self.checkTree(pRoot1.left, pRoot2.left) and self.checkTree(pRoot1.right, pRoot2.right)
#         else:
#             return res or self.checkTree(pRoot1.left, pRoot2) or self.checkTree(pRoot1.right, pRoot2)

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # pRoot1 = TreeNode(8)
# # pRoot1.left = TreeNode(8)
# # pRoot1.right = TreeNode(7)
# # pRoot1.left.left = TreeNode(9)
# # pRoot1.left.right = TreeNode(2)
# # pRoot1.left.right.left = TreeNode(4)
# # pRoot1.left.right.right = TreeNode(7)

# # pRoot2 = TreeNode(8)
# # pRoot2.left = TreeNode(9)
# # pRoot2.right = TreeNode(2)

# pRoot1 = TreeNode(8)
# pRoot1.left = TreeNode(8)
# pRoot1.right = TreeNode(7)
# pRoot1.left.left = TreeNode(9)
# pRoot1.left.right = TreeNode(2)
# pRoot1.left.right.left = TreeNode(4)
# pRoot1.left.right.right = TreeNode(7)

# pRoot2 = TreeNode(8)
# pRoot2.left = TreeNode(9)
# pRoot2.right = TreeNode(2)

# a = Solution()
# b = a.hasSubtree(pRoot1, pRoot2)
# print(b)

##################### 69

# class Solution(object):
#     def getNumberSameAsIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         left = 0
#         right = len(nums) - 1
#         res = (left + right)//2
        
#         while left <= right:
#             if nums[res] == res:
#                 return res
#             elif nums[res] > res:
#                 right = res - 1
#                 res = (left + right)//2
#             else:
#                 left = res + 1
#                 res = (left + right)//2
        
#         return -1

# nums = [1,2,3]
# a = Solution()
# b = a.getNumberSameAsIndex(nums)
# print(b)

#################################
# n = 0
# a = [9]
# b = [0]
# for i in range(1,10):
#     a.append((i+1) * 9 * 10 ** i + a[-1])
#     b.append((i + 1) * 10 ** i - a[-2] - 1)

# for i in range(10):
#     if n < a[i]:
#         num = str((n + b[i]) // (i+1))
#         j = (n + b[i]) % (i+1)
#         print(num[j])

# print(a,b)

############################ 53

# class Solution(object):
#     def getLeastNumbers_Solution(self, input, k):
#         """
#         :type input: list[int]
#         :type k: int
#         :rtype: list[int]
#         """
#         res = [float('inf')]*k

#         for i in range(len(input)):
#             if input[i] < res[k-1]:
#                 res = self.reshape(res, input[i])
        
#         return res
    
#     def reshape(self, res, k):
#         for i in range(len(res)):
#             if res[i] > k:
#                 res.insert(i,k)
#                 res.pop()
#                 return res

# a = Solution()
# input = range(10)
# k = 4
# b = a.getLeastNumbers_Solution(input,k)
# print(b)


#################################

# class Solution(object):
#     def lastRemaining(self, n, m):
#         """
#         :type n: int
#         :type m: int
#         :rtype: int
#         """
#         nums = list(range(n))
#         return self.deleteNum(nums,m)
        
#     def deleteNum(self,nums,m):
#         if len(nums) == 1:
#             return nums[0]
#         else:
#             if m >= len(nums):
#                 m %= len(nums)
#             nums[:] = nums[m + 1:] + nums[:m]
#             return self.deleteNum(nums,m) 

# n = 5
# m = 3

# a = Solution()
# b = a.lastRemaining(n,m)
# print(b)

######################

# class Solution:
#     def __init__(self):
#         self.nums = []
#     def insert(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         res = []
#         for i in range(len(num)):
#             if self.nums == []:
#                 self.nums.append(num[i])
#                 res.append(self.getMedian)
#             elif num[i] > self.nums[-1]:
#                 self.nums.append(num[i])
#                 res.append(self.getMedian)
#             else:
#                 for j in range(len(self.nums)):
#                     if num[i] <= self.nums[j]:
#                         self.nums.insert(j,num[i])
#                         break
#                 res.append(self.getMedian)
        
#     def getMedian(self):
#         """
#         :rtype: float
#         """
#         n = len(self.nums)
#         if n%2 == 1:
#             return self.nums[n//2]
#         else:
#             return (self.nums[n//2] + self.nums[n//2 - 1])/2

# num = [-3, -1, 1, 0, -4]
# # m = 3

# a = Solution()
# b = a.insert(num)
# print(b)


#########################

# nums = [3, 32, 321]
# class Solution(object):
#     def printMinNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: str
#         """
#         if nums == []: return ''
#         nums = self.strReshape(nums)
#         nums = self.bubble_sort(nums)
#         return ''.join(nums)
        
#     def bubble_sort(self, nums):
#         for i in range(len(nums) - 1): 
#             for j in range(len(nums) - i - 1): 
#                 if nums[j] + nums[j + 1] > nums[j + 1] + nums[j]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         return nums
    
#     def strReshape(self, nums):
#         tmp = []
#         for i in range(len(nums)):
#             tmp.append(str(nums[i]))
#         return tmp

# a = Solution()
# b = a.printMinNumber(nums)
# print(b)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def printFromTopToBottom(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if not root: return []
        
#         res = []
#         Tree = [root]
#         layer = 0

#         while Tree:
#             res1 = []
#             Tree1 = []

#             for i in range(len(Tree)):
#                 if layer % 2 == 0:
#                     res1.append(Tree[i].val)
#                 else:
#                     res1.append(Tree[-i - 1].val)

#                 if Tree[i].left:
#                     Tree1.append(Tree[i].left)
#                 if Tree[i].right:
#                     Tree1.append(Tree[i].right)

#             res.append(res1)
#             Tree = Tree1
#             layer += 1

#         return res

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# tree = TreeNode(9)
# tree.right = TreeNode(16)
# tree.right.left = TreeNode(7)
# tree.right.right = TreeNode(12)
# tree.right.left.left = TreeNode(14)
# tree.right.right.right = TreeNode(11)
# tree.right.left.left.left = TreeNode(2)

# a = Solution()
# b = a.printFromTopToBottom(tree)
# print(b)

#################################

# class Solution:
#     def getTranslationCount(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         num = str(s)
        
#         if len(num) in [0, 1]:
#             return len(num)
        
#         res = [0, 1]
        
#         for i in range(1, len(num)):
            
#             if int(num[i-1:i+1]) < 26 and int(num[i-1]) != 0:
#                 res.append(res[-1] + res[-2])
#             else:
#                 res.append(res[-1])
                
#         return res[-1]

# s = 70476768
# a = Solution()
# b = a.getTranslationCount(s)
# print(b)

#################

# class Solution:
#     def longestSubstringWithoutDuplication(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         st = {}
#         first,length = 0,0

#         for i in range(len(s)):
#             if s[i] in st:
#                 first = max(st[s[i]],first)
#             length = max(length,i - first + 1)
#             st[s[i]] = i + 1
        
#         return length    

# s = 'asdfdasf'
# a = Solution()
# b = a.longestSubstringWithoutDuplication(s)
# print(b)

#########################

# class Solution(object):
#     def getMaxValue(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         m = len(grid)
#         n = len(grid[0])
        
#         res = [[0] * n for i in range(m)]
        
#         for i in range(m):
#             for j in range(n):
                
#                 if i == 0 and j == 0:
#                     res[0][0] = grid[0][0]
#                 elif i == 0:
#                     res[i][j] += res[i][j-1] + grid[i][j]
#                 elif j == 0:
#                     res[i][j] += res[i-1][j] + grid[i][j]
#                 else:
#                     res[i][j] = max(res[i][j-1], res[i-1][j]) + grid[i][j]
                    
#         return res[m - 1][n - 1]

# grid = [[4, 7, 4], [9, 7, 7]]

# a = Solution()
# b = a.getMaxValue(grid)
# print(b)

##########################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def findPath(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: List[List[int]]
#         """
            
#         res = []
#         result = []
#         self.checkPath(root, sum, res, result)
#         return result
        
#     def checkPath(self, root, sum, res, result):
#         if not root:
#             return None
            
#         res.append(root.val)
#         sum -= root.val

#         if sum == 0:
#             if not root.left or not root.right:
#                 result.append(res[:])

#         if root.left:
#             self.checkPath(root.left, sum, res, result)
#         if root.right:
#             self.checkPath(root.right, sum, res, result)
        
#         res.pop()



# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# root = None
# # root = TreeNode(6)
# # root.right = TreeNode(2)
# # root.right.left = TreeNode(3)
# # root.right.left.right = TreeNode(2)
# # root.right.right = TreeNode(5)

##############

# class Solution(object):
#     def numberOf1Between1AndN_Solution(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         res = 0
        
#         for i in range(n + 1):
#             res += self.check(i)
#         return res
        
#     def check(self, n):
#         res = 0
        
#         while n != 0:
#             if n % 10 == 1:
#                 res += 1
            
#             n //= 10
        
#         return res

# n = 1
# a = Solution()
# b = a.numberOf1Between1AndN_Solution(n)
# print(b)

####################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def __init__(self):
#         self.res = []
#         self.head = None
#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return self.res
#         else:
#             self.res.append(root.val)
#             return self.seializeCore([root])
    
#     def seializeCore(self, Tree):
        
#         if not Tree:
#             return self.res
#         else:
#             newTree = []
#             for i in range(len(Tree)):
#                 if Tree[i].left:
#                     self.res.append(Tree[i].left.val)
#                     newTree.append(Tree[i].left)
#                 else:
#                     self.res.append(None)
                    
#                 if Tree[i].right:
#                     self.res.append(Tree[i].right.val)
#                     newTree.append(Tree[i].right)
#                 else:
#                     self.res.append(None)
#             Tree = newTree
#             return self.seializeCore(Tree)

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data:
#             return self.head
#         else:
#             self.head = TreeNode(data[0])
#             data.pop(0)
#             return self.deserializeCore([self.head], data)
    
#     def deserializeCore(self, tree, data):
        
#         if not data:
#             return self.head
#         else:
#             newtree = []
#             for i in range(len(tree)):
#                 if data[0]:
#                     tree[i].left = TreeNode(data[0])
#                     newtree.append(tree[i].left)
#                 data.pop(0)
#                 if data[0]:
#                     tree[i].right = TreeNode(data[0])
#                     newtree.append(tree[i].right)
#                 data.pop(0)
#             tree = newtree
#             return self.deserializeCore(tree, data)

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root = TreeNode(6)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# root.right.left.right = TreeNode(2)
# root.right.right = TreeNode(5)

# a = Solution()
# b = a.serialize(root)
# c = [6, None, 2, 3, 5, None, 2, None, None, None, None]
# d = a.deserialize(c)
# print(b)
# print(d)

##########################

# class Solution:
#     def firstNotRepeatingChar(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         d = {}
#         for i in range(len(s)):
#             if s[i] in d.keys():
#                 d[s[i]] += 1
#             else:
#                 d[s[i]] = 1

#         s = list(d.keys())
#         for i in range(len(s)):
#             if d[s[i]] == 1:
#                 return s[i]
        
#         return '#'
# s = 'fsafg'
# a = Solution()
# b = a.firstNotRepeatingChar(s)
# print(b)

############################

# class Solution: 
#     def __init__(self):
#         self.d = {}
#         self.k = []
        
#     def firstAppearingOnce(self):
#         """
#         :rtype: str
#         """
#         for i in range(len(self.k)):
#             if self.d[self.k[i]] == 1:
#                 return self.k[i]
        
#         return '#'
        
#     def insert(self, char):
#         """
#         :type char: str
#         :rtype: void
#         """
#         if char in self.k:
#             self.d[char] += 1
#         else:
#             self.d[char] = 1
#             self.k.append(char)

# a = Solution()
# a.insert('1')
# print(a.firstAppearingOnce())

############################

# class Solution(object):
#     def getNumberOfK(self, nums, k):
#         """
#         :type nums: list[int]
#         :type k: int
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         left = 0
#         right = len(nums)
#         mid = (left + right) // 2
#         midnum = -1
        
#         while left <= right:
#             if nums[mid] < k:
#                 left = mid + 1
#                 mid = (left + right) // 2
#             elif nums[mid] > k:
#                 right = mid - 1
#                 mid = (left + right) // 2
#             else:
#                 midnum = mid
#                 break
        
#         if midnum == -1:
#             return 0
            
#         leftIndex = self.getLeft(midnum, nums, k)
#         rightIndex = self.getRight(midnum, nums, k)
#         return rightIndex - leftIndex + 1
        
#     def getLeft(self, midnum, nums, k):
#         left = 0
#         right = midnum
#         mid = (left + right)//2

#         while left < right:
#             if nums[mid] == k:
#                 right = mid
#             else:
#                 left = mid + 1
#             mid = (left + right) // 2
        
#         return right

#     def getRight(self, midnum, nums, k):
#         left = midnum
#         right = len(nums) - 1
#         mid = (left + right)//2

#         if nums[right] == k:
#             return right

#         while left < right:
#             if nums[mid] == k:
#                 left = mid
#                 mid = (left + right) // 2
#                 right -= 1
#             else:
#                 right = mid - 1
#                 mid = (left + right) // 2
            
        
#         return left

# nums = [0,0,0,0,1,1,1,2,2,2,2,2,2]
# k = 2
# a = Solution()
# b = a.getNumberOfK(nums, k)
# print(b)

################################

# class Solution(object):
#     def findContinuousSequence(self, k):
#         """
#         :type sum: int
#         :rtype: List[List[int]]
#         """

#         if k <= 2:
#             return []

#         left = k // 2
#         right = left + 1
#         res = []

#         while left >= 1:
#             if sum(list(range(left, right + 1))) == k:
#                 res.append(list(range(left, right + 1)))
#                 left -= 1
#             elif sum(list(range(left, right + 1))) < k:
#                 right += 1
#             else:
#                 left -= 1
#                 right -= 1

#         return res


################################

# class Solution(object):
#     def numberOfDice(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """

#         res = []

#         for i in range(1, n + 1):
#             if i == 1:
#                 res = [1] * 6
#             else:
#                 res = self.newRes(res, i)

#         return res

#     def newRes(self, res, n):
#         newres = [0] * (5 * n + 1)
#         for i in range(6):
#             for j in range(len(res)):
#                 newres[i + j] += res[j]
#         return newres


# class Solution(object):
#     def findNumsAppearOnce(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = 0
        
#         for i in range(len(nums)):
#             res ^= nums[i]
        
#         index = 0

#         while (res & 1) == 0:
#             res >>= 1
#             index += 1
#         a = b = 0
#         for i in nums:
#             if self.fun(i, index):
#                 a ^= i
#             else:
#                 b ^= i
#         return [a, b]

#     def fun(self, num, index):
#         num = num >> index
#         return num & 1

############################

# class Solution(object):
#     def strToInt(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         if not str: return 0
#         length = len(str)

#         nums = '0123456789'

#         i = 0
#         while str[i] == ' ' and i <= length - 1:
#             i += 1
            
#         num = ''
#         flag = 1
        
#         if i == length - 1:
#             return 0
            
#         if str[i] == '+':
#             flag = 1
#             i += 1
#         elif str[i] == '-':
#             flag = -1
#             i += 1
#         while i <= length - 1 and str[i] in nums:
#             num += str[i]
#             i += 1
            
#         n = int(num) * flag
        
#         if n > 2**31 - 1:
#             return 'INT_MAX'
#         elif n < - 2 ** 31:
#             return 'INT_MIN'
            
#         return n

# str = 'la123'  
# a = Solution()
# b = a.strToInt(str)
# print(b)

##########################

# class Solution(object):
#     def isContinuous(self, numbers):
#         """
#         :type numbers: List[int]
#         :rtype: bool
#         """
#         numbers.sort()
#         KingNum = 0
#         n = 0
#         d = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#         if numbers == [] or numbers == [0] * 5:
#             return False
            
#         for i in range(5):
#             if numbers[i] == 0:
#                 KingNum += 1
#             elif numbers[i] not in d or numbers[i] == numbers[i-1]:
#                 return False
#             elif n == 0:
#                 n = d.index(numbers[i]) + 1
#             elif numbers[i] in d:
#                 if numbers[i] == d[n]:
#                     n += 1
#                 elif numbers[i] - d[n] <= KingNum:
#                     KingNum -= numbers[i] - d[n]
#                     n += numbers[i] - d[n] + 1
#                 else:
#                     return False

#             else:
#                 return False
        
#         return True

# a = Solution()
# numbers = [0,1,3,5,0]
# b = a.isContinuous(numbers)
# print(b)
##############################
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if (root.left == p and root.right == q) or (root.left == q and root.right == p):
#             return root
#         elif not root.left or not root.right:
#             if root.left:
#                 return self.lowestCommonAncestor(root.left, p, q)
#             elif root.right:
#                 return self.lowestCommonAncestor(root.right, p, q)
#             else:
#                return None
#         else:
#             self.lowestCommonAncestor(root.left, p, q)
#             self.lowestCommonAncestor(root.right, p, q)

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# a = Solution()
# root = TreeNode(1)
# p = None
# q = None
# b = a.lowestCommonAncestor(root,p,q)
# print(b)

######################################

# class Solution(object):
#     def findNumberAppearingOnce(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         s = [0] * 5
#         n = 0
        
#         for i in range(len(nums)):
#             s = self.addNum(nums[i], s)
            
#         for j in range(len(s)):
#             n = n * 10 + s[j] % 3
            
#         return int(str(n), 2)
            
#     def addNum(self, n, s):
#         i = -1
#         while n != 0:
#             if n & 1 == 1:
#                 s[i] += 1
#             n >>= 1
#             i -= 1
            
#         return s

# a = Solution()
# nums = [1,1,1,2,2,2,3,4,4,4]
# b = a.findNumberAppearingOnce(nums)
# print(b)

######################

# class Solution(object):
#     def isPopOrder(self, pushV, popV):
#         """
#         :type pushV: list[int]
#         :type popV: list[int]
#         :rtype: bool
#         """
#         res = []
#         while pushV or popV:
#             if pushV and pushV[0] == popV[0]:
#                 pushV.pop(0)
#                 popV.pop(0)
#             elif res and popV[0] == res[-1]:
#                 res.pop()
#                 popV.pop(0)
#             elif pushV:
#                 res.append(pushV[0])
#                 pushV.pop(0)
#             else:
#                 return False
#         if not res:
#             return True
#         else:
#             return False


##############################

# class Solution:
#     def verifySequenceOfBST(self, sequence):
#         """
#         :type sequence: List[int]
#         :rtype: bool
#         """
#         if not sequence:
#             return True
            
#         index = len(sequence) - 1
        
#         for i in range(len(sequence)):
#             if sequence[i] > sequence[-1]:
#                 index = i
#                 break
                
#         for i in range(index, len(sequence)):
#             if sequence[i] < sequence[-1]:
#                 return False
                
#         return self.verifySequenceOfBST(sequence[:index]) and self.verifySequenceOfBST(sequence[index:-1])

# class Solution(object):
#     def __init__(self):
#         self.count = 0

#     def kthNode(self, pRoot, k):
#         if not pRoot:
#             return None
#         node = self.kthNode(pRoot.left, k)
#         if node:
#             return node
#         self.count += 1
#         if self.count == k:
#             return pRoot
#         node = self.kthNode(pRoot.right, k)
#         if node:
#             return node
        
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tree = TreeNode(2)
# Tree.left = TreeNode(1)
# Tree.right = TreeNode(3)
# a = Solution()
# sequence = [2,1,3]
# b = a.kthNode(Tree, 3)
# print(b)

#######################################

# class Solution(object):
#     def strToInt(self, s):
#         """
#         :type str: str
#         :rtype: int
#         """

#         n = ''
#         index = 0
#         length = len(s)
#         d = '0123456789'
#         flag = 1
#         last = ' '

#         while index < length:
#             if last == ' ' and s[index] in d:
#                 break
#             elif s[index] == '-':
#                 flag = -1
#                 index += 1
#                 break
#             elif s[index] == '+':
#                 flag = 1
#                 index += 1
#                 break
#             else:
#                 last = s[index]
#                 index += 1

#         while index < length and s[index] in d:
#             n += s[index]
#             index += 1

#         if n == '':
#             return 0
#         else:
#             n = int(n) * flag

#         if n > 2 ** 31 - 1:
#             return 'INT_MAX'
#         elif n < - 2 ** 31:
#             return 'INT_MIN'
#         else:
#             return n

# a = Solution()
# b = a.strToInt('la123')
# print(b)

###########################


# def findKthUgly(k):
#     ugly = []
#     ugly.append(1)
#     index = 1
#     index2 = 0
#     index3 = 0
#     index5 = 0
#     while index < k:
#         val = min(ugly[index2]*2, ugly[index3]*3, ugly[index5]*5)
#         if ugly[index2]*2 == val:
#             index2 += 1
#         if ugly[index3]*3 == val:
#             index3 += 1
#         if ugly[index5]*5 == val:
#             index5 += 1
#         ugly.append(val)
#         index += 1
#     return ugly[-1]

# print(findKthUgly(20))


##################################

# class Solution(object):
#     def add(self, num1, num2):
#         """
#         :type num1: int
#         :type num2: int
#         :rtype: int
#         """

#         while num2:
#             num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, ((num1 & num2) << 1) & 0xFFFFFFFF

#         return num1 if  num1 <= 0x7FFFFFFF else ~(num1^0xFFFFFFFF)

# a = Solution()
# b = a.add(2147483647, -4)
# print(b)

#########################################
# import os
# import pandas as pd
# unames = ['text']
# users = pd.read_table('test.dat',sep='::',header=None,names=unames)
# text = 'Title="example: 2d finite-element data"\n\
# variables ="x","y","S1"\n\
# zone N=8,E=3, datapacking=block\n\
# varlocation=([3]=cellcentered)\n\
# zonetype=fequadrilateral\n\
# 0 0 0 0 1 1 1 1 \n\
# 0 1 2 3 0 1 2 3\n\
# 10\n\
# -5\n\
# 1.0\n\
# 1 5 6 2\n\
# 2 6 7 3\n\
# 3 7 8 4\n'

# f = open("test.dat", "r+")

# f.write(text)
# f.close
# print(text)


################################### 108

# nums = [-10,-3,0,5,9]

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def sortedArrayToBST(self, nums):
        
#         if not nums:
#             return None 
#         n = len(nums) // 2
#         head = TreeNode(nums[n])
#         head.left = self.sortedArrayToBST(nums[:n])
#         head.right = self.sortedArrayToBST(nums[n + 1:])

#         return head

# a = Solution()
# b = a.sortedArrayToBST(nums)
# print('finish')

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         if not headA or not headB:
#             return None
        
#         hA = []
#         hB = []
#         node = None

#         while not headA:
#             hA.append(headA)
#             headA = headA.next
        
#         while not headB:
#             hB.append(headB)
#             headB = headB.next

#         while len(hA)>0 and len(hB) > 0:
#             a = hA.pop()
#             b = hB.pop()

#             if a == b:
#                 node = a
#             else:
#                 break
        
#         return node
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# headA = ListNode(4)
# headA.next = ListNode(1)
# headB = ListNode(5)
# headB.next = ListNode(1)

# a = Solution()
# b = a.getIntersectionNode(headA, headB)

# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         d = {}
#         for i in range(len(s)):

#             if s[i] in d:
#                 if d[s[i]] == t[i]:
#                     continue
#                 else:
#                     return False
#             else:
#                 if t[i] in d.values():
#                     return False
#                 d[s[i]] = t[i]

#         return True

# a = Solution()
# b = a.isIsomorphic('ab', 'aa')
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head:
#             return None
            
#         tail = head
#         length = 1

#         while tail.next:
#             tail = tail.next
#             length += 1

#         k %= length

#         if k == 0:
#             return head

#         breaknode = head
#         while k != 1:
#             breaknode = breaknode.next
#             k -= 1

#         newhead = breaknode.next
#         breaknode.next = None
#         tail.next = head

#         return newhead



# head = ListNode(1)
# head.next = ListNode(2)

# a = Solution()
# b = a.rotateRight(head, 1)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:

#     def binaryTreePaths(self, root):
#         res = []
#         if not root:
#             return res
#         self.core(root, [], res)
#         return res

#     def core(self, root, path, res):

#         path.append(root.val)
        
#         if not root.left and not root.right:
#             res.append(path)
#             path.pop()
#             return 

#         if root.left:
#             self.core(root.left, path, res)
#         if root.right:
#             self.core(root.right, path, res)
            

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)

# a = Solution()
# b = a.binaryTreePaths(root)
# print(b)


# class Solution:
#     def generateMatrix(self, n):
#         matrix = []
#         lo = n*n + 1

#         while lo > 1:
#             lo, hi = lo - len(matrix), lo
#             a = [list(range(lo, hi))]
#             b = list(zip(*matrix[::-1]))
#             matrix = a + b
#         return matrix

# a = Solution()
# b = a.generateMatrix(3)
# print(b)

# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """


#         return s

# a = Solution()
# b = a.reverseVowels('hello')
# print(b)


# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.minNum = []

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.stack.append(x)
#         if not self.minNum:
#             self.minNum.append(x)
#         elif x < self.minNum[-1]:
#             self.minNum.append(x)
#         else:
#             self.minNum.append(self.minNum[-1])
        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         if not self.stack:
#             return None
#         self.minNum.pop()
#         return self.stack.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         if not self.stack:
#             return None
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         if not self.stack:
#             return None
#         return self.minNum[-1]

# a = MinStack()
# a.push(-2)
# a.push(0)
# a.push(-3)
# print(a.pop())
# print(a.top())
# print(a.getMin)

# # 一个二叉树样例
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)

# class Solution:

#     def binaryTreePaths(self, root):

#         if not root:
#             return []
#         res = []
#         self.core(root,'',res)
#         return res

#     def core(self, root, path, res):
#         path += str(root.val)
#         if not root.left and not root.right:
#             res.append(path)

#         if root.left:
#             self.core(root.left, path + '->', res)

#         if root.right:
#             self.core(root.right, path + '->', res)

# class Solution:
#     def sumOfLeftLeaves(self, root):
#         if not root:
#             return 0
        
#         num = 0
#         num = self.sumCore(root, num, 0)
#         return num
    
#     def sumCore(self, root, num, flag):

#         if not root.left and not root.right:
#             num += root.val * flag
            
        
#         if root.left:
#             num = self.sumCore(root.left, num, 1)
#         if root.right:
#             num = self.sumCore(root.right, num, 0)

#         return num
# a = Solution()
# b = a.sumOfLeftLeaves(root)
# print(b)

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         d = {}
#         length = [0]

#         for i in range(len(s)):
#             if s[i] not in d:
#                 d[s[i]] = i
#                 length.append(length[-1] + 1)
#             else:
#                 length.append(max(length[-1], i - d[s[i]]))
#                 d[s[i]] = i
        
#         return max(length)

# a = Solution()
# b = a.lengthOfLongestSubstring("pwwkew")
# print(b)

# class Solution:
#     def isNumber(self, s: str) -> bool:
#       #define a DFA
#       state = [{}, 
#               {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
#               {'digit':3, '.':4},
#               {'digit':3, '.':5, 'e':6, 'blank':9},
#               {'digit':5},
#               {'digit':5, 'e':6, 'blank':9},
#               {'sign':7, 'digit':8},
#               {'digit':8},
#               {'digit':8, 'blank':9},
#               {'blank':9}]
#       currentState = 1
#       for c in s:
#           if c >= '0' and c <= '9':
#               c = 'digit'
#           if c == ' ':
#               c = 'blank'
#           if c in ['+', '-']:
#               c = 'sign'
#           if c not in state[currentState].keys():
#               return False
#           currentState = state[currentState][c]
#       if currentState not in [3,5,8,9]:
#           return False
#       return True


# a = Solution()
# b = a.isNumber("  +323123.e12103")
# print(b)

# class Solution:
#     def findNthDigit(self, n: int) -> int:
#         # a = []
#         # b = []
#         # for i in range(10):
#         #     a.append(9 * 10 ** i)
#         #     b.append((i + 1) * 10 ** i - a[i])
            
#         # if n <= 9:
#         #     return n
#         # elif n <= 189:
#         #     num = str((n + 10)//2)
#         #     i = 1 - (n + 9) % 2
#         #     return num[i]
#         # elif n <= 2889:
#         #     num = str((n + 110) // 3)
#         #     i = 2 - (n + 191) % 3
#         #     return num[i]
#         # elif n <= 38889:
#         #     num = str((n + 1110) // 4)
#         #     i = 3 - (n + 1110) % 4
#         #     return num[i]
#         a = [9]
#         b = [0]
#         for i in range(1,10):
#             a.append((i+1) * 9 * 10 ** i + a[-1])
#             b.append((i + 1) * 10 ** i - a[-2] - 1)
        
#         for i in range(10):
#             if n <= a[i]:
#                 num = str((n + b[i]) // (i+1))
#                 j = (n + b[i]) % (i+1)
#                 return num[j]

# a = Solution()
# b = a.findNthDigit(9)
# print(b)

# class Solution:
#     def readBinaryWatch(self, num):
#         hour = 0
#         minute = num - hour
#         res = []

#         while 0 <= hour <= 3:
#             if minute >= 6:
#                 hour += 1
#                 minute -= 1
#             elif minute < 0:
#                 break
#             else:
#                 hours = self.Hours(hour)
#                 minutes = self.Minutes(minute)

#                 for i in hours:
#                     for j in minutes:
#                         res.append(i +':' + j)
#                 hour += 1
#                 minute -= 1
        
#         return res

#     def Hours(self, hour):
#         if hour == 0:
#             return ['0']
#         elif hour == 1:
#             return ['1', '2', '4', '8']
#         elif hour == 2:
#             return ['3', '5', '6', '9', '10']
#         elif hour == 3:
#             return ['7', '11']

#     def Minutes(self, minutes):
#         res = []
#         for i in range(60):
#             m = i
#             n = 0
#             while m != 0:
#                 n += m & 1
#                 m >>= 1
#             if n == minutes:
#                 if i < 10:
#                     res.append('0' + str(i))
#                 else:
#                     res.append(str(i))
#         return res

# a = Solution()
# b = a.readBinaryWatch(3)
# print(b)

# # 一个二叉树样例
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(1)
# root.right.right = TreeNode(11)
# class Solution(object):
#     def pathSum(self, root, s):
#         return self.helper(root, s, [s])

#     def helper(self, node, origin, targets):
#         if not node: return 0
#         hit = 0
#         for t in targets:
#             if not t-node.val: hit += 1                          # count if sum == target
#         targets = [t-node.val for t in targets]+[origin]         # update the targets
#         return hit+self.helper(node.left, origin, targets)+self.helper(node.right, origin, targets)

# a = Solution()
# b = a.pathSum(root, 8)
# print(b)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res = ''

#         for i in range(len(s)):
#             tmp = self.helper(s,i,i)
#             if len(tmp) > len(res):
#                 res = tmp
#             tmp = self.helper(s,i,i+1)
#             if len(tmp) > len(res):
#                 res = tmp
#         return res

#     def helper(self,s,i,j):
#         while i >= 0 and j < len(s) and s[i] == s[j]:
#             i -= 1; j += 1
#         return s[i-1:j]

# a = Solution()
# b = a.longestPalindrome("babad")

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         res = 0
#         flag = 1
#         symbol = 0
#         for i in range(len(s)):

#             if s[i] == ' ':
#                 continue

#             if s[i] == '+' or s[i] == '-':
#                 if s[i] == '+' and symbol == 0:
#                     flag = 1
#                     symbol = 1
#                     continue
#                 elif s[i] == '-' and symbol == 0:
#                     flag = -1
#                     symbol = 1
#                     continue
#                 else:
#                     return res
            
                
            
#             if s[i] <'0' or s[i]>'9':
#                 break
#             else:
#                 res = res*10 + int(s[i])

#         res *= flag

#         if res > 2 ** 31 - 1:
#             return 2 ** 31 - 1
#         elif res < - 2 ** 31:
#             return - 2 ** 31
#         else:
#             return res

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         state = [{}, 
#             {'blank': 1, 'sign': 2, 'digit':3, 'alphabet':4}, 
#             {'digit':3},
#             {'digit':3, 'alphabet':5, 'blank':5},
#             {'digit':3, 'sign':2, 'alphabet':4},
#             {'alphabet':5}]
#         currentState = 1
#         res = ''
#         for c in s:
#             if c == ' ':
#                 b = 'blank'
#             elif c >= '0' and c <= '9':
#                 b = 'digit'
#             elif c == ' ':
#                 b = 'blank'
#             elif c in ['+', '-']:
#                 b = 'sign'
#             else:
#                 b = 'alphabet'
#             if b not in state[currentState].keys():
#               return 0
#             currentState = state[currentState][b]
#             if currentState in [2,3]:
#                 res += c
#         if currentState not in [3,5]:
#             return 0
#         res = int(res)
#         if res > 2 ** 31 - 1:
#             return 2 ** 31 - 1
#         elif res < - 2 ** 31:
#             return - 2 ** 31
#         else:
#             return res

# a = Solution()
# b = a.myAtoi('4193 with words')
# print(b)

# class Solution:
#     def nextPermutation(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         minNum = nums[-1]
#         length = len(nums)
#         flag = 0

#         for i in range(1, length + 1):
#             if nums[-i] < minNum:
#                 d = nums[length-i:]
#                 a = max(d)
#                 d.remove(a)
#                 d.sort()
#                 nums = nums[0:length-i] + [a] + d
#                 flag = 1
#                 break
#             else:
#                 minNum = nums[-i]

#         if not flag:
#             nums.sort()
        
#         return nums

# a = Solution()
# b = a.nextPermutation([1,2,3])
# print(b)

# class Solution(object):
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         length = [[0] * len(grid[0]) for i in range(len(grid))]
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if i == 0 and j == 0:
#                     length[i][j] = grid[i][j]
#                 elif i == 0:
#                     length[i][j] = length[i][j-1] + grid[i][j]
#                 elif j == 0:
#                     length[i][j] = length[i-1][j] + grid[i][j]
#                 else: 
#                     length[i][j] = min(length[i-1][j], length[i][j-1]) + grid[i][j]

#         return length[i][j]

# a = Solution()
# b = a.minPathSum([[1,2,5],[3,2,1]])
# print(b)

# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])

#         d = [[0] * n for i in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     d[i][j] = obstacleGrid[i][j] ^ 1
#                 elif i == 0:
#                     d[i][j] = d[i][j-1] * (obstacleGrid[i][j-1] ^ 1)
#                 elif j == 0:
#                     d[i][j] = d[i-1][j] * (obstacleGrid[i-1][j] ^ 1)
#                 else: 
#                     d[i][j] = d[i-1][j] * (obstacleGrid[i-1][j] ^ 1) + d[i][j-1] * (obstacleGrid[i][j-1] ^ 1)
#                     # 位运算优先级低于加减法运算

#         return d[i][j] * (obstacleGrid[i][j] ^ 1)
# a = Solution()
# b = a.uniquePathsWithObstacles([[0,1],[0,0]])
# print(b)

# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return nums[0]
        
#         curMax = nums[0]
#         curMin = nums[0]
#         ans = nums[0]

#         for i in range(1, len(nums)):
#             curMax, curMin = max(curMax * nums[i], curMin * nums[i], nums[i]), min(curMax * nums[i], curMin * nums[i], nums[i])
#             ans = max(curMax, ans)
        
#         return ans

# a = Solution()
# b = a.maxProduct([-4,-3,-2])

class Solution(object):
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]

a = Solution()
b = a.wordBreak("aaaaaaa",["aaaa","aaa"])
print(b)