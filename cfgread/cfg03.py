with open("vlanconfig.cfg", "r") as configfile:
    configlist= configfile.readlines()
print(configlist)
print(f"Number of lines: {len(configlist)}")
