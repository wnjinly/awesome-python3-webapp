import os
import time
import zipfile
import shutil

source = r'/Users/water/project/pythonStudy'

target_dir = r'/Users/water/project/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = now + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)

comment = raw_input('Enter a comment -->')

if len(comment) == 0:
    target = now + '.zip'
else:
    target = now + '_' + comment.replace(' ', '_') + '.zip'

z = zipfile.ZipFile(target, 'w')
for dirpath, dirname, filenames in os.walk(source):
    for filename in filenames:
        z.write(os.path.join(dirpath, filename))
z.close()

if os.path.exists(today):
    shutil.move(target, today)
    print('backup successfully')
