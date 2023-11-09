# create, write, read, delete, update, 

'''
Hello everyone, this is our introduction lesson
Let us get started with Python programming


'''
from datetime import datetime

now = datetime.now().strftime("%d %b %Y %H:%M")
f = open('sample.txt', 'a')
f.write(f'This should have a time stamp - {now} \n')
f.close()

