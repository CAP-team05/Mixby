filename = 'links.txt'
f = open(filename, 'r')
links = f.readlines()

for link in links:
    link = link.split('LM')[1]
    code = link.split('?')[0]
    print(code)