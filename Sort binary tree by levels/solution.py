from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    
    res = []
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        
        res.append(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return res
