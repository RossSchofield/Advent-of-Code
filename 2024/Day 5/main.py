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


for update in updates:
    pages = [int(page) for page in update.split(',')]
    seen = set()
    for page in pages:
        seen.add(page)
        if page in rules.keys():
            if seen.intersection(rules[page]):
                break
    else:
        middle_page = pages[len(pages)//2]
        middle_pages.append(middle_page)

print(sum(middle_pages))