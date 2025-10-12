def maxFreqSum(s: str) -> int:
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    cons = {}

    for char in s:
        if char in vowels:
            vowels[char] += 1 
        else:
            cons[char] = cons.get(char, 0) + 1

    score = max(vowels.values(), default = 0) + max(cons.values(), default = 0) 
    return score

print(maxFreqSum("aeiaaioooaauuaeiu"))  # Output: 6
print(maxFreqSum("abcde"))            # Output: 2
print(maxFreqSum("leetcode"))        # Output: 4
print(maxFreqSum("rhythm"))        # Output: 2

