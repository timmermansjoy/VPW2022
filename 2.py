def score(persoon):
    persoon_score = 0
    if "DNF" in persoon:
        persoon_score = None
    else:
        persoon = [float(x) for x in persoon]
        persoon_score += sum(persoon)
    return persoon_score




cases = int(input())

for i in range(cases):
    vijand = sorted(input().split())
    jij = sorted(input().split())

    vijand = sorted([float(x) for x in vijand if x != "DNF"])
    if len(vijand) <=3:
        vijand_score = None
    elif len(vijand) == 4:
        vijand = vijand[1:5]
        print(vijand)
        vijand_score = sum(vijand)
    else:
        vijand = vijand[1:4]
        vijand_score = sum(vijand)

    jij = sorted([float(x) for x in jij if x != "DNF"])
    if len(jij) <=2:
        jij_score = None
    elif len(jij) == 3:
        jij_beste = jij[0]
        jij_slechtste = 600.00
        jij = jij[1:4]
        jij_score = sum(jij)
    else:
        jij_beste = jij[0]
        jij_slechtste = jij[-1]
        print(jij_slechtste)
        jij = jij[1:3]
        jij_score = sum(jij)


    if vijand == None:
         if jij == None:
             print(i+1, "onmogelijk nog te winnen")
         else:
            print(i+1, 600.00)

    else:
        if jij == None:
            print(i+1,"onmogelijk nog te winnen")
        else:
            total_score = (round(vijand_score - jij_score,2) - 0.01)
            if total_score >= jij_slechtste:
                print(i+1 , ("reeds gewonnen"))
            elif total_score <= jij_beste:
                print(i+1, "onmogelijk nog te winnen")
            else:
                print(i+1, round(total_score,2))
