def findLucky(arr) -> int:
        dict = {}
        for num in arr:
            counter = arr.count(num)
            if counter > 1: 
                dict[num] = counter

        if not dict:
            return -1
        biggest_num = max(dict.keys()) 
        biggest_count = max(dict.values())

        if dict[biggest_num] == biggest_count:
            return biggest_num
        else:
            return -1       
        
print(findLucky([2,2,3,4]))
print(findLucky([1,2,2,3,3,3]))
print(findLucky([2,2,2,3,3]))
print(findLucky([5]))       