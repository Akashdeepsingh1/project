from collections import defaultdict


def avgMarks(result):
    if not result:
        return 0
    total_marks = defaultdict(int)
    total_course = defaultdict(int)

    for k, v in result:
        total_marks[k] = total_marks[k] + v
        total_course[k] += 1
    max_avg = 0
    student_name = ""
    for k, v in total_marks.items():
        temp_avg = v/total_course[k]
        if max_avg < temp_avg:
            max_avg = temp_avg
            student_name = k

    print(f'The {student_name} has got max avg of {max_avg}')


result = [("James", 70), ("Fernando", 90), ("Nick", 60), ("James", 10)]
avgMarks(result)
