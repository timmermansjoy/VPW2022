
cases = int(input())


for _ in range(cases):
    K,R = input().split()
    holes = 0
    for i in range(int(R)):
        rij = input()
        found_star = False
        for j in rij:
            if j != '.':
                found_star = True
            else:
                if found_star:
                    holes += 1
    print(_+1, holes)
