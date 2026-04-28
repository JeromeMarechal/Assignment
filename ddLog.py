# Two daily logs of (userId, pageId) pairs.
# Return the list of users who visited on both days and accessed ≥2 distinct pages across the two days.
 
#day_one = [[1,1],[2,1]]
#day_two = [[1,1],[2,2]]
day_one = [[1, 1], [1, 2],[2, 1]]
day_two = [[1, 3],[2, 2]]

log = [day_one, day_two]

def get_count_user_pages(report):
    max_pages = max(len(data[0]) for data in report.values())
    return [userId for userId, data in report.items() if len(data[0]) == max_pages]

def get_count_user_day(report):
    max_day = max(data[1] for data in report.values())
    return [userId for userId, data in report.items() if data[1] == max_day]

def collect_data(report, day):
    for userId, pageId in day:
        if userId not in report:
            report[userId] = [set(), 0]
        report[userId][0].add(pageId)
        report[userId][1] += 1


def is_loyal_customer(log):
    report = {}
    day_count = 0

    for day in log:
        collect_data(report, day)
        day_count += 1

    max_days = get_count_user_day(report)
    max_pages = get_count_user_pages(report)

    result = [userId for userId in max_days if userId in max_pages]
    print(result)
    
is_loyal_customer(log)



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
            report[userId] = [set(), set()]
        report[userId][0].add(pageId)
        report[userId][1].add(2)
    day_count += 1    

    #print(report)
    #print(day_count)
    result = [userId for userId, data in report.items() if len(data[0]) > 1 and max(data[1]) == day_count]
    print(result)

is_loyal_customer(day_one, day_two)    


# Two daily logs of (userId, pageId) pairs.
# Return the list of users who visited on both days and accessed ≥2 distinct pages across the two days.

day_one = [[1, 1], [2, 2]]
day_two = [[2, 2],[2, 1],[1, 2],[2, 1]]

def is_loyal_customer(day_one, day_two):
    report = {}
    result = set() # change to list

    for userId, pageId in day_one:
        if userId not in report:
            report[userId] = set()
        report[userId].add(pageId)

    # if len(day_two) < 2 and report[day_two[0][1]] not in report[day_two[0][0]]:
    #     return [day_two[0][0]]
    # else:
    for userId, pageId in day_two:
        if userId not in report:
            continue
            # report[userId] = set()
        report[userId].add(pageId)
        if len(report[userId]) >= 2:
            result.add(userId)

    return result


loyal_user = is_loyal_customer(day_one, day_two)
print(loyal_user)

