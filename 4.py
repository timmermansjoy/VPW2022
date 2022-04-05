
cases = int(input())

for i in range(cases):

    w, o, hw, ho = input().split()
    # make int of all
    w = int(w)
    o = int(o)
    hw = int(hw)
    ho = int(ho)

    if hw > ho:
        while w>hw and w!=o:
            o += 1
            w -= 1


    elif ho > hw:
        while o>ho and o!=w:
            w += 1
            o -= 1

    else:
        if not (o <= ho and w <= hw):
            o = 1
            w = 1

    if o == w:
        print(i+1, "gelijk")

    else:
        print(i+1, f"{w} {o}")
