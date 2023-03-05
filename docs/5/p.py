f = open("./in.txt", "r")
for line in f:
    if line.replace("\n", "") != "":
        if line.replace("\n", "").startswith("    "):
            print("            - " + line.replace("\n", "")) 
        elif not line.replace("\n", "").startswith("    "):
            print("        - " + line.replace("\n", "")) 