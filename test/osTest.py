import os

for dirpath, dirnames, filenames in os.walk('./images'):
    print(len(filenames))
    for filename in filenames:
        b=str(os.path.join(dirpath, filename)).replace('\\','/')
        print(b)
