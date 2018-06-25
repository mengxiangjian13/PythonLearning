import shutil
import os

for fileDir, subDirs, filenames in os.walk('.'):
    for filename in filenames:
        # print(os.path.join(fileDir,filename))
        if not os.path.exists('./tm'):
            os.mkdir('./tm')
        if fileDir.endswith == '/tm':
            continue
        if filename.endswith('.txt') or filename.endswith('.md'):
            shutil.copy(os.path.join(fileDir,filename),'./tm')