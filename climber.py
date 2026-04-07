def climber(n: int) -> int:
    if n < 0:
        return "Error: n must be a non negative INT"
    
    if n > 0:
        start, suite = 1, 1
        for i in range(n - 1):
            start, suite = suite, start + suite
        return suite
        



# examples:
print(climber(2))  # Output: 2
print(climber(3))  # Output: 3
print(climber(4))  # Output: 5
print(climber(5))  # Output: 8
print(climber(6))  # Output: 13
print(climber(7))  # Output: 21
print(climber(8))  # Output: 34 
print(climber(9))  # Output: 55            