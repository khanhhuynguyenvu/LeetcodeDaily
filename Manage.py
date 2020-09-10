file = open("Solved.txt", "r")
links = []
for line in file.readlines():
    line = line.replace(chr(10), "")
    links.append(line)


def find(link):
    return list(filter(lambda key: key == link, links)) != []


def manage_processed():
    file = open("Processed.txt", "a")
    file.truncate(0)
    for line in sorted(links):
        file.write(line + "\n")
    file.close()


manage_processed()
