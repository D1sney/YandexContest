
def students_and_computers():
    n1, n2 = map(int, input().split())
    stu = list(map(int, input().split()))
    com = list(map(int, input().split()))

    stud = sorted(((stu[i], i) for i in range(len(stu))), key=lambda x: x[0], reverse=True)
    comp = sorted(((com[i], i) for i in range(len(com))), key=lambda x: x[0], reverse=True)

    result = [0] * n1
    done = 0

    c = 0
    for s in range(n1):
        if comp[c][0] >= stud[s][0]+1:
            result[stud[s][1]] = comp[c][1] + 1
            c += 1
            done += 1
    
    print(done)
    print(*result, end=' ')

students_and_computers()