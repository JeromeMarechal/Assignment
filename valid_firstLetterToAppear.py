def repeatedCharacter(s: str) -> str:
    char = {}

    for i in range(len(s)):
        if s[i] in char.keys() and char[s[i]] != 2:
            char[s[i]] += 1

        if s[i] in char and char[s[i]] == 2:
            return s[i]

        elif s[i] not in char.keys():
            char[s[i]] = 1

    return None

# Examples:
print(repeatedCharacter("abccbaacz"))  # Output: "c"
print(repeatedCharacter("abcdd"))      # Output: "d"
print(repeatedCharacter("abcd"))       # Output: None
print(repeatedCharacter("aabbcc"))     # Output: "a"