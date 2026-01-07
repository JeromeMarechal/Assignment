# Two daily logs of (userId, pageId) pairs.
# Return the list of users who visited on both days and accessed ≥2 distinct pages across the two days.
 
#day_one = [[1,1],[2,1]]
#day_two = [[1,1],[2,2]]
day_one = [[1, 1], [1, 2],[2, 1]]
day_two = [[1, 3],[2, 2]]

def is_loyal_customer(day_one, day_two):
    report = {}
    day_count = 0

    for userId, pageId in day_one:
        if userId not in report:
            report[userId] = [set(), set()]
        report[userId][0].add(pageId)
        report[userId][1].add(1)
    day_count += 1    

    for userId, pageId in day_two:
        if userId not in report:
            report[userId] = [set(), 0]
        report[userId][0].add(pageId)
        report[userId][1].add(2)
    day_count += 1    

    #print(report)
    #print(day_count)
    result = [userId for userId, data in report.items() if len(data[0]) > 1 and max(data[1]) == day_count]
    print(result)

is_loyal_customer(day_one, day_two)    

