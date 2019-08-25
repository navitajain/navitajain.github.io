# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # DFS iterative
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # root None
            return 0
        depth = [(root,1)]     # stack LIFO
        max_ht = 1
        while depth:
            n = depth.pop(0)     # stack LIFO
            node,depth_ht = n[0],n[1]
            if max_ht < depth_ht:     
                max_ht = depth_ht
            if node.right:
                depth.insert(0,(node.right,depth_ht+1))  
            if node.left:
                depth.insert(0,(node.left,depth_ht+1))    # #LIFO insert left child last so it's first out
        return max_ht
                
    # BFS iterative
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # root None
            return 0
        level = [root]   #queue FIFO
        lvl_no = 0
        while level:      # until all levels are covered
            lvl_no += 1
            cnodes = []  #queue FIFO , at each level create a single array for the childnodes
            for l in level:             # cover all nodes at a level
                if l.left:
                    cnodes.append(l.left)    
                if l.right:
                    cnodes.append(l.right)   # append child nodes to the queue
            level = cnodes    #move to next level
        return lvl_no
    
    # recursive
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # root None
            return 0
        
        return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))