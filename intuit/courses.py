import collections
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]
def courseOverlaps(studentCoursePairs):
    if not studentCoursePairs: return
    student_courses = collections.defaultdict(set)
    for student, course in studentCoursePairs:
        student_courses[student].add(course)
    seen = set()
    for s1 in student_courses.keys():
        for s2 in student_courses.keys():
            if s1 != s2 and (s1, s2) not in seen and (s2, s1) not in seen:
                seen.add((s1, s2))
                print('[{}, {}]: {}'.format(s1, s2, list(student_courses[s1] & student_courses[s2])))

courseOverlaps(student_course_pairs_1)


def courseSchedule1(courseRelation):
    allCourses = set()
    pre = collections.defaultdict(set)
    is_pre = collections.defaultdict(set)
    for i, j in courseRelation:
        allCourses.add(i)
        allCourses.add(j)
        is_pre[j].add(i)
        pre[i].add(j)
    res = []
    seen = set()
    dq = collections.deque([i for i in allCourses if not pre[i]])
    while dq:
        cur = dq.popleft()
        if cur in seen: continue
        seen.add(cur)
        res.append(cur)
        for nei in is_pre[cur]:
            pre[nei].remove(cur)
            if not pre[nei]:
                dq.append(nei)
    return res if len(seen) == len(allCourses) else []

print(courseSchedule1([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('Z', 'Y'), ('Z', 'X'), ('Z', 'G')]))
print(courseSchedule1([('A', 'B'), ('B', 'A')]))

def courseHelper(coursesRelation):
    # time: O(V! + E) space: O(V + E)
    allCourses = set()
    pre = collections.defaultdict(set)
    is_pre = collections.defaultdict(set)
    for i, j in coursesRelation:
        allCourses.add(i)
        allCourses.add(j)
        is_pre[j].add(i)
        pre[i].add(j)

    res = set()

    def dfs(path, seen, course):
        if len(path) == len(allCourses):
            res.add(tuple(path))
            return
        if course in seen or pre[course]:
            return
        mark = set()
        for i in is_pre[course]:
            pre[i].discard(course)
            mark.add(i)
        for i in allCourses - seen:
            dfs(path + [course], seen | {course}, i)
        for i in mark:
            pre[i].add(course)

    for i in allCourses:
        dfs([], set(), i)

    return res

all_courses = [
    ["Logic","COBOL"],
    ["Data Structures","Algorithms"],
    ["Creative Writing","Data Structures"],
    ["Algorithms","COBOL"],
    ["Intro to Computer Science","Data Structures"],
    ["Logic","Compilers"],
    ["Data Structures","Logic"],
    ["Creative Writing","System Administration"],
    ["Databases","System Administration"],
    ["Creative Writing","Databases"]
]
all_courses2 = []
for c in all_courses:
    all_courses2.append(c[::-1])
for x in courseHelper(all_courses2):
    print(len(x))

print({x[len(x) // 2] for x in courseHelper(all_courses2)})



