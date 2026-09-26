# https://leetcode.com/problems/parallel-courses-iii/


def minimum_time(courses, relation, time):
    def status_update(course, rem, ongoing,month):
        # 3 status C,O,N (completed, ongoing and not started)
        if course not in rem:
            return 'C'
        if course in ongoing :
            if ongoing[course]==month:
                ongoing.pop(course)
                rem.remove(course)
                return 'C'
            else:
                return 'O'
        return 'N'


    # set which contains all the remaining courses which are not completed or ongoing
    rem = {course for course in range(1,courses+1)}
    # contains all courses which are ongoing
    ongoing = dict()

    month = 0

    while len(rem)>0:
        for course in range(1,courses+1):
            if status_update(course, rem,ongoing,month) in ('C','O'):
                continue
            can_start = True
            for rel in relation:
                if rel[1] == course:
                    pre = rel[0]
                    if status_update(pre, rem,ongoing,month) in ('O','N'):
                        can_start=False
                        break
            if can_start:
                ongoing[course] = month + time[course-1]
        if len(rem):
            month+=1

    return month

courses = int(input('Enter the number of courses : '))
relation = eval(input('Enter the relation between courses : '))
time = eval(input('Enter the duration of courses : '))

print(minimum_time(courses,relation,time))