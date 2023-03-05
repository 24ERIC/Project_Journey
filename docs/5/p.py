f1 = open("./compare.txt", "r")
f2 = open("./in.txt", "r")

for line1 in f1:
    line1 = line1.replace("\n", "")
    for line2  in f2:
        line2 = line2.replace("\n", "")
        if (line1 == line2):
            break
    if line1 != line2:
        print(line1)




# f1 = open("./compare.txt", "r")
# for line in f1:
#     if line[1:3] == "h2":
#         continue
#     line = line.replace("<br/>", "").replace("\n", "")
#     print(line)