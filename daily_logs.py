# Two daily logs of (userId, pageId) pairs.
# Return the list of users who visited on both days and accessed ≥2 distinct pages across the two days.
 
day_one = [[1,1],[2,1]]
day_two = [[1,1],[2,2]]
#day_one = [[1, 1], [1, 2],[2, 1]]
#day_two = [[1, 3],[2, 2]]

def is_loyal_customer(day_one, day_two):
    report = {}
    result = []

    for userId, pageId in day_one:
        if userId not in report:
            report[userId] = set()
        report[userId].add(pageId)

    if len(day_two) < 2 and report[day_two[0][1]] not in report[day_two[0][0]]:
        return [day_two[0][0]]
    else :
        for userId, pageId in day_two:
            if userId not in report:
                report[userId] = set()
            report[userId].add(pageId)
            if len(report[userId]) >= 2:
                result.append(userId)
        return result        

loyal_user = is_loyal_customer(day_one, day_two)
print(loyal_user)

