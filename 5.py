
cases = int(input())


for i in range(cases):
    score = 10
    Wolk, Mist, Neerslag, Wind = [int(x) for x in input().split()]

    # clamp wolk to 0-8
    Wolk = max(0, min(8, Wolk))
    # clamp mist to 0-12
    Mist = max(0, min(12, Mist))
    # clamp neerslag to 0-720
    Neerslag = max(0, min(720, Neerslag))
    # clamp wind to 0-12
    Wind = max(0, min(12, Wind))


    # Wolk
    if 1 < Wolk <= 5:
        score -= 1
    elif 5 < Wolk <= 7:
        score -= 2
    elif 7 < Wolk:
        score -= 3

    # Mist
    if 0 < Mist < 6:
        score -= 1
    elif 6 <= Mist:
        score -= 2

    # Neerslag
    if 10 <= Neerslag < 90:
        score -= 1
    elif 90 <= Neerslag < 300:
        score -= 2
    elif 300 <= Neerslag < 500:
        score -= 3
    elif 500 <= Neerslag:
        score -= 4

    # Wind
    if Wind == 3:
        score -= 1
    elif Wind == 4 or Wind == 5:
        score -= 2
    elif 6 <= Wind:
        score -= 3

    print(i+1, max(1,score))
