with open("dracula.txt", "r") as dracula_file:
    dracula_content = dracula_file.readlines()
vampire_lines=[]
for line in dracula_content:
    if 'vampire' in line.lower():
        print(line.strip())
        vampire_lines.append(line)
print(f"Number of lines:{len(vampire_lines)}")
with open("vampytimes.txt","w") as vampytimes_file:
    vampytimes_file.writelines(vampire_lines)
