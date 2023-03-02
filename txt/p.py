inlines = open("./input.txt", "r")
for inline in inlines:
    if not inline.startswith("•   "):
        print("- " + inline[:-2]) 

    else:
        t = inline.split("•   ")[1]
        tt = t.split("   ")
        tt[1] = tt[1][:-2]
        tt1 = "[" + tt[0] + "]" + "(" + tt[1] + ")"
        print("    - " + tt1)
        # if (len(tt) == 1):
        #     print(tt)