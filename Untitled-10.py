import os

a = os.listdir()
for filename in a:
    if os.path.isdir(filename):
        continue
    f = open(filename, 'r')
    try:
        print(f.read())
    except:
        print(filename + ' read error')
    finally:
        f.close()