def writeToFile(filename, content, delimiter='\n', mode='a'):
    with open(filename, mode, encoding="utf-8") as f:
        f.write(content + delimiter)
writeToFile('a1.md', '', '', 'w')
writeToFile('a2.md', '', '', 'w')

with open('a.md', 'r', encoding='utf-8') as f:
    raw = f.read()
for row in raw.split('\n'):
    if '=' in row:
        writeToFile('a1.md', row)
        writeToFile('a3.md', row)
    else: 
        writeToFile('a2.md', ' = '.join(row.split(' ', 1)))
        writeToFile('a3.md', ' = '.join(row.split(' ', 1)))