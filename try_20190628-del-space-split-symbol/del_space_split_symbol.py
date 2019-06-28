for line in open("element.txt", "r"):
    data = line.lstrip()

    file1 = open("id.txt", "a")
    file1.write(data[0:9])
    file1.close()