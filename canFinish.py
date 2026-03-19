def canFinish(numCourses, prerequisites) -> bool:
    list_of_list = [[] for _ in range(numCourses)]
    for course, pre in prerequisites:
        list_of_list[course].append(pre)

    state = [0] * numCourses

    def depth_search(course):
        if state[course] == 1:
            return False
        
        if state[course] == 2:
            return True
        
        if state[course] == 0:
            state[course] = 1
            for pre in list_of_list[course]:
                if depth_search(pre) == False:
                    return False
            state[course] = 2
            return True
        
    for course in range(numCourses):
        if depth_search(course) == False:
            return False

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

