definitions = []

file = open('dictionary.txt', 'r')

for line in file:
    definitions.append(line.split(' ', maxsplit=1)[1].replace('"','').rstrip())
print(definitions)
