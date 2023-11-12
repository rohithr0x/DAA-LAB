n, d = map(int, input("Enter n,d : ").split())
teachers = []
for _ in range(n):
    di, ti, si = map(int, input("Enter di, ti, si : ").split())
    teachers.append((di, ti, si))

teachers.sort(key=lambda x: x[0])

curse_level = 0
for teacher in teachers:
    di, ti, si = teacher
    for _ in range(ti):
        if di <= d:
            di += 1
        else:
            curse_level += si
            break
print(curse_level)
