def climbStairs(n: int) -> int:
    arr = [0, 1]
    
    for i in range(n):
        arr.append(arr[i] + arr[i+1])
        
    print(arr)    
    return arr[-1]
        
    
    
# examples:
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
print(climbStairs(4))  # Output: 5
print(climbStairs(5))  # Output: 8
print(climbStairs(6))  # Output: 13
print(climbStairs(7))  # Output: 21
print(climbStairs(8))  # Output: 34 
print(climbStairs(9))  # Output: 55
