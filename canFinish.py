def canFinish(numCourses, prerequisites) -> bool:
    if len(prerequisites) < 2:
        return True
    
    path = set()
    
    for pair in prerequisites:
        if pair[1] in path:
            if pair[0] in path:
                return False
        path.add(pair[0])
    return True
        
            
            
    
    
          
    
    
# Examples:
print(canFinish(2, [[1,0]]))  # True
print(canFinish(2, [[1,0],[0,1]]))  # False
print(canFinish(3, [[0,1],[0,2],[1,2]]))  # True
print(canFinish(3, [[0,1],[1,2],[2,0]]))  # False
print(canFinish(4, [[0,1],[1,2],[2,3],[3,1]]))  # False
print(canFinish(5, [[0,1],[1,2],[2,3],[3,4]]))  # True
print(canFinish(2, [[0,1],[1,0]]))  # False    
print(canFinish(12, [[1,0],[2,1],[3,2],[4,3],[5,4],[6,5],[7,6],[8,7],[9,8],[10,9],[11,10]]))  # True