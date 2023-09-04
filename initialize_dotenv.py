with open(".env", "r") as f:
    list_of_lines = f.readlines()

list_of_lines = [f'{line.split("=")[0]}=\n' for line in list_of_lines]

with open(".env.sample", "w") as f:
    for line in list_of_lines:
        f.write(line)

