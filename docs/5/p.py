f = open("./in.txt", "r")
for line in f:
    if line.replace("\n", "") != "":
        line = line.replace("\n", "").replace("* ", "- ").replace("TryHackMe | ", "")
        if line[0:3] == "---":
            continue
        elif line[0] == "-":
            print(line.replace("\n", "").replace("- ", "            - "))
        elif line[0] == "#":
            print(line.replace("\n", "").replace("## ", "        - "))
        
        line = line.replace("            - [", "").replace(")", "")
        if line.startswith("        - "):
            continue
        if "]" in line:
            i = line.index("]")
            line = line[i+2:]
        print(line)