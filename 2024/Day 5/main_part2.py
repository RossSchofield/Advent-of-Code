rules = {}
updates = []
middle_pages = []

with open('input.txt') as file:
    while (line := file.readline().strip()) != '':
        before, after = [int(page) for page in line.split('|')]
        if before not in rules.keys():
            rules[before] = set()
        rules[before].add(after)

    for line in file:
        updates.append(line.strip())

def check_update_valid(rules, pages):

    seen = set()
    for i, page in enumerate(pages):
        seen.add(page)
        if page in rules.keys():
            if seen.intersection(rules[page]):
                return i
    else:
        return -1


for update in updates:
    pages = [int(page) for page in update.split(',')]

    invalid_page = check_update_valid(rules, pages)
    if invalid_page != -1:
        while invalid_page != -1:
            temp = pages[invalid_page]
            pages[invalid_page] = pages[invalid_page-1]
            pages[invalid_page-1] = temp
            invalid_page = check_update_valid(rules, pages)
    else:
        continue

    middle_page = pages[len(pages) // 2]
    middle_pages.append(middle_page)


print(sum(middle_pages))