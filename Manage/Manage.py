from time import sleep

file = open("C:/Users/huynvk/Desktop/LeetcodeDaily/Manage/Solved.txt", "r")
links = []


def put_links():
    for line in file.readlines():
        line = line.replace(chr(10), "")
        links.append(line)
    return 1


def find(link):
    return list(filter(lambda key: key == link, links)) != []


def manage_processed():
    file = open("Processed.txt", "a")
    file.truncate(0)
    for line in sorted(links):
        file.write(line + "\n")
    file.close()


def to_processed_log():
    # print(links)
    if len(links) == 0:
        idx = 0
        while idx != 1:
            idx = put_links()
        # sleep(2)
    # print(links)
    log_processed = []
    for line in links:
        log = line.split(",")
        link, tags, level, frequency = log[0], log[1:len(log) - 2], log[-2], log[-1]
        tags = ",".join(tags)
        frequency = float(frequency)
        log_processed.append(tuple([link, tags, level, frequency]))
        # print(log_processed[-1])
    return log_processed


# put_links()
to_processed_log()
