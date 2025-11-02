def repeatedCharacter( s: str) -> str:
    char = {}

    for i in range(len(s)):
        if s[i] in char.keys() and char[s[i]][1] != 2:
            char[s[i]][0] = i - char[s[i]][0]
            char[s[i]][1] += 1
        elif s[i] not in char.keys():
            char[s[i]] = [i, 1]

    char = {pairs: values[0] for pairs, values in char.items() if values[1] == 2}
    
    if char:
        min_distance = min(char.values())
    else:
        return None
    
    for char, distance in char.items():
        if distance == min_distance:
            return char
        

# Examples: 
print(repeatedCharacter("abccbaacz"))  # Output: "c"
print(repeatedCharacter("abcdd"))      # Output: "d"
print(repeatedCharacter("abcd"))       # Output: None
print(repeatedCharacter("aabbcc"))    # Output: "a"    
           