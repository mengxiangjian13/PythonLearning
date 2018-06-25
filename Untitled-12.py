import os

desktop = '/Users/mengxiangjian/Desktop'
for folder, subFolders, filenames in os.walk(desktop):
    for name in filenames:
        fullname = os.path.join(folder,name)
        if os.path.exists(fullname):
            size = os.path.getsize(fullname)
            if size > 100000000: # size大于100M
                print(fullname)
        