with open('klm.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

# finally, write lines in the file
with open('klm.txt', 'w') as f:
    f.writelines(lines)