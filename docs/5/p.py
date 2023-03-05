f = open("./in.txt", "r")
for line in f:
    if line.replace("\n", "") != "":
        line = line.replace("\n", "").replace("* ", "-")
        if line[0:3] == "---":
            continue
        elif line[0] == "-":
            print(line.replace("\n", "").replace("- ", "            - "))
        elif line[0] == "#":
            print(line.replace("\n", "").replace("## ", "        - "))