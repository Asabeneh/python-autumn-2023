import os

f = open('obama_speech.txt')
txt = f.read().replace('\n', ' ').replace(',', '').replace('.', '').replace('?','').replace('-', '').lower()
words = txt.split()

print(txt)
# lines = f.readlines()
# for line in lines:
#     print(line.strip().split())
""" if os.path.exists('test-folder') == False:
    os.mkdir('test-folder')
if os.path.exists('test-folder'):
    os.rmdir('test-folder') """
test = os.walk('.')
for item in test:
    r, d, files = item
    for filename in files:
        if filename.endswith('.txt'):
            f = open(filename)
            txt = f.read()
            words = txt.strip().lower().split()
            print(words)


